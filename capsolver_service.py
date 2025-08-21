import json, time, os, sys
from typing import Optional, Union
from simplelogger import SimpleLogger
from curl_cffi_session import createSession

class CapsolverService:
    def __init__(self, api_key: str, logger: Optional[Union[SimpleLogger]] = None):
        if not api_key:
            raise Exception("api_key is None")
        self.api_key = api_key
        self.logger = logger or SimpleLogger()
        self.session = createSession(logger=self.logger)

    def create_task(self, website_url: str, website_key: str, page_action: str | None, type: str = "ReCaptchaV3Task", enterprise_payload: Optional[dict] = None, cookies: Optional[list[dict]] = None, proxy: Optional[str] = None, anchor: Optional[str] = None, reload: Optional[str] = None) -> str:
        """
        Creates a task for solving a captcha.

        Args:
            website_url (str): The URL of the website where the captcha is located.
            website_key (str): The key associated with the captcha on the website.
            page_action (str | None): The action to be performed on the page, if applicable.
            type (str): The type of captcha task. Defaults to "ReCaptchaV3Task".
            enterprise_payload (Optional[dict]): Additional payload for enterprise captcha solving, if applicable.
            cookies (Optional[list[CapsolverCookie]]): A list of cookies to be used in the task. Each cookie should be a dictionary with 'name' and 'value' keys.
            proxy (Optional[str]): The proxy to be used for the task, if applicable.
            anchor (Optional[str]): The anchor value to be used for the task
            reload (Optional[str]): The reload value to be used for the task

        Returns:
            str: The task ID for the created captcha solving task.
        """

        payload = {
                    "clientKey": self.api_key,
                    "task": {
                            "type": type,
                            "websiteURL": website_url,
                            "websiteKey": website_key,
                            "pageAction": page_action,
                            "enterprisePayload": enterprise_payload,
                            "cookies": cookies,
                            "proxy": proxy,
                            "anchor": anchor,
                            "reload": reload,
                            }
                    }

        headers = {"Content-Type": "application/json"}
        response = self.session.request_with_retries(
                                                        url="https://api.capsolver.com/createTask",
                                                        method="POST",
                                                        data=json.dumps(payload),
                                                        headers=headers
                                                    ).json()

        if response.get("errorId") != 0:
            raise Exception(f"Error creating task: {response}")

        task_id = response.get("taskId")
        self.logger.info(f"Task created successfully with taskId: {task_id}, type: {type}")
        return task_id

    def get_task_result(self, task_id: str) -> str:
        payload = {
                    "clientKey": self.api_key,
                    "taskId": task_id
                }

        headers = {"Content-Type": "application/json"}
        response = self.session.request_with_retries(
                                                        url="https://api.capsolver.com/getTaskResult",
                                                        method="POST",
                                                        data=json.dumps(payload),
                                                        headers=headers
                                                    ).json()

        if response.get("errorId") != 0:
            raise Exception(f"Error fetching task result: {response}")

        if response.get("status") == "ready":
            token = response["solution"]["gRecaptchaResponse"]
            self.logger.info(f"Task result ready, token: {token[:15]}")
            return token
        else:
            raise Exception(f"Task result not ready, status: {response.get('status')}")

    def solve_captcha(self, website_url: str, website_key: str, page_action: str | None, type: str = "ReCaptchaV3Task", enterprise_payload: Optional[dict] = None, cookies: Optional[list[dict]] = None, proxy: Optional[str] = None, anchor: Optional[str] = None, reload: Optional[str] = None, max_retry_result = 10) -> str:
        task_id = self.create_task(website_url, website_key, page_action, type, enterprise_payload, cookies, proxy, anchor, reload)
        retries = 0
        while retries < max_retry_result:
            try:
                return self.get_task_result(task_id)
            except Exception as e:
                retries += 1
                self.logger.info(f"Task result not ready yet, retrying in 1 second... Attempt {retries}/{max_retry_result}. Error: {e}")
                time.sleep(1)
        raise Exception("Max retries reached, task result not ready.")
    



