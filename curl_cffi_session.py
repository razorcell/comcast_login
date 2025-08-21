from curl_cffi import requests
import time
from curl_cffi.requests.exceptions import (
    RequestException,
    HTTPError,
    ConnectionError,
    Timeout,
)
from typing import Any, Optional


class CurlCffiSession(requests.Session):
    def __init__(self, logger: Optional[Any] = None, **kwargs):
        super().__init__(**kwargs)
        self.logger = logger or self._default_logger()

    def _default_logger(self):
        class DefaultLogger:
            def info(self, msg: str):
                print(f"INFO: {msg}")

            def warning(self, msg: str):
                print(f"WARNING: {msg}")

            def error(self, msg: str):
                print(f"ERROR: {msg}")

        return DefaultLogger()

    def request_with_retries(
        self,
        url: str,
        method: str = "GET",
        ignore_status_codes: list = [],
        test: bool = False,
        response_validator: Optional[Any] = None,
        **kwargs,
    ) -> requests.Response:
        max_retry = kwargs.pop("max_retry", 7)
        backoff_factor = kwargs.pop("backoff_factor", 1)
        ignore_status_codes = ignore_status_codes or []

        for attempt in range(max_retry):
            try:
                if test:
                    # Manually construct the headers to include cookies
                    headers = kwargs.get("headers", {})
                    cookies = self.cookies.get_dict()
                    # headers.update({'Cookie': '; '.join([f"{k}={v}" for k, v in cookies.items()])})
                    for key, value in cookies.items():
                        self.logger.info(f"Cookie: {key}={value}")
                    self.logger.info(
                        f"URL: {url},\n"
                        f"Request details:\n"
                        f"Method: {method},\n"
                        f"Headers: {headers},\n"
                        f"Params: {kwargs.get('params')},\n"
                        f"Json: {kwargs.get('json')},\n"
                        f"Data: {kwargs.get('data')}"
                    )

                response = self.request(method, url, verify=False, **kwargs)  # type: ignore
                if response.status_code in ignore_status_codes:
                    self.logger.info(f"Status code {response.status_code} ignored.")
                    return response

                response.raise_for_status()  # Raise an error for bad responses

                if response_validator and not response_validator(
                    response=response, logger=self.logger
                ):
                    raise RequestException("Response validation failed.")

                return response
            # except (RequestException, HTTPError, ConnectionError, Timeout) as e:
            except Exception as e:
                wait_time = backoff_factor * (2**attempt)
                if attempt < max_retry - 1:
                    error_type = type(e).__name__
                    error_msg = str(e)

                    # Log proxy information if it's a proxy connection error
                    if "Proxy CONNECT aborted" in error_msg:
                        proxy = kwargs.get("proxies", {})
                        sanitized_proxy = self.sanitize_proxy(proxy)
                        self.logger.warning(
                            f"Proxy connection error. Proxy settings: {sanitized_proxy}"
                        )

                    self.logger.warning(
                        f"Attempt {attempt + 1} failed with {error_type}: {e}. URL: {url}, Retrying in {wait_time} seconds..."
                    )
                    time.sleep(wait_time)  # Exponential backoff
                else:
                    self.logger.error(
                        f"Attempt {attempt + 1} failed with error: {e}. No more retries left."
                    )
                    e.response = response if "response" in locals() else None  # type: ignore
                    raise e
        return response

    def sanitize_proxy(self, proxy: dict[str, str]) -> dict[str, str]:
        sanitized_proxy = {}
        for key, value in proxy.items():
            if key.lower() in ["http", "https"]:
                parts = value.replace("http://", "").split("@")
                if len(parts) == 2:
                    user_pass, address = parts
                    user, password = user_pass.split(":")
                    sanitized_user = user[:2] + "****"
                    sanitized_password = "****" + password[-2:]
                    sanitized_value = f"{sanitized_user}:{sanitized_password}@{address}"
                else:
                    sanitized_value = value
                sanitized_proxy[key.lower()] = sanitized_value
            else:
                sanitized_proxy[key.lower()] = value.strip()
        return sanitized_proxy

    def set_cookies(self, cookies: dict):
        for key, value in cookies.items():
            self.cookies.set(key, value)


def createSession(logger: Optional[Any] = None, **kwargs) -> CurlCffiSession:
    return CurlCffiSession(logger=logger, **kwargs)


def extract_cookies_from_response(response: requests.Response, logger=None) -> dict:
    if logger is None:
        logger = CurlCffiSession()._default_logger()
    cookies = {}

    # Extract session cookies from the response
    response_cookies = response.cookies
    for key, value in response_cookies.items():
        cookies[key] = value

    # Extract set-cookies from response headers
    set_cookie_header = response.headers.get_list(
        "Set-Cookie"
    ) or response.headers.get_list("set-cookie")
    for cookie in set_cookie_header:
        cookie_parts = cookie.split(";")  # type: ignore
        for part in cookie_parts:
            if "=" in part:
                key, value = part.split("=", 1)
                cookies[key.strip()] = value.strip()

    if not cookies:
        raise Exception("No cookies were extracted from the response.")

    # logger.info("Extracted cookies: " + json.dumps(cookies, indent=4))

    return cookies
