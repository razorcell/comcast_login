import json
import os
from typing import List, Optional
from comcast_service import fill_input_field
from curl_cffi_session import CurlCffiSession
from simplelogger import SimpleLogger
from capsolver_service import CapsolverService
from united_master_types import TaskSettings
from botasaurus.browser import browser, Driver, Wait

# Browser Based Method

def handle_cookies_accept(driver: Driver):
    try:
        driver.wait_for_element("#onetrust-accept-btn-handler", Wait.SHORT)
        if driver.select("#onetrust-accept-btn-handler"):
            driver.click("#onetrust-accept-btn-handler")
        else:
            print("No cookie accept button found.")
    except Exception as e:
        print(f"Exception occurred while handling cookies: {e}. This is acceptable if the accept button is not present.")


def navigate_to_united_master(driver: Driver):
    try:
        driver.google_get("https://unitedmasters.com/")
        driver.short_random_sleep()
        print("Navigated to United Master Business website.")
    except Exception as e:
        print(f"Error navigating to United Master Business website: {e}")


def click_a_button(driver: Driver, selector: str):
    try:
        driver.short_random_sleep()
        driver.wait_for_element(selector, Wait.SHORT)
        button = driver.select(selector)
        if button:
            print("button found:", button)
            driver.click(selector)
            print("Clicked the button.")
        else:
            print(f"button not found. selector: {selector}")
    except Exception as e:
        print(f"Error interacting with Next button: {e}")

def click_next_button(driver: Driver):
    try:
        driver.short_random_sleep()
        next_button = driver.get_element_with_exact_text("Next")

        if next_button:
            print("Next button found:", next_button)
            next_button.click()
            print("Clicked the Next button.")
        else:
            print("Next button not found.")
    except Exception as e:
        print(f"Error interacting with Next button: {e}")


def handle_login(driver: Driver):
    username = os.getenv("UNITED_MASTER_USERNAME")
    if username:
        fill_input_field(driver, "input[id='email']", username, "USERNAME")
    else:
        print("USERNAME not found in environment variables.")

    driver.short_random_sleep()

    password = os.getenv("UNITED_MASTER_PASSWORD")
    if password:
        fill_input_field(driver, "input[id='password']", password, "PASSWORD")
    else:
        print("PASSWORD not found in environment variables.")

    driver.short_random_sleep()

    click_next_button(driver)


# HTTP requests method

def get_residential_proxies() -> dict:
    """
    Retrieves residential proxy settings from environment variables.

    Returns:
        dict: A dictionary containing 'http' and 'https' proxy settings.
    """
    http_proxy = os.getenv("RESIDENTIAL_PROXY")

    if not http_proxy:
        raise Exception("Residential proxies are not properly set in the environment variables.")

    return {
        "http": http_proxy,
        "https": http_proxy
    }


def visit_united_master_home_page(session: CurlCffiSession, logger: SimpleLogger) -> str:
    """
    Visits the home page of United Masters using the provided session.

    Args:
        session: The Curl CFFI session to use for making the request.

    Returns:
        str: The response text from the home page.

    Raises:
        Exception: If the request fails.
    """
    url = "https://unitedmasters.com/"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
    }

    response = session.request_with_retries(
        url=url,
        method="GET",
        headers=headers,
        proxies=get_residential_proxies(),
        impersonate="chrome",
    )
    
    if response.status_code != 200:
        raise Exception(f"Failed to visit home page. Status code: {response.status_code}, Response: {response.text}")
    
    logger.info(f"Visited United Masters home page. Status code: {response.status_code}")
    logger.info(f"Response headers: {response.headers}")
    logger.info(f"Response text snippet: {response.text[:200]}")  # Log the first 200 characters of the response text
    cookies = session.cookies.get_dict()
    if cookies:
        logger.info("Session cookies:")
        for key, value in cookies.items():
            logger.info(f"  {key}: {value}")
    else:
        logger.info("No cookies found in the session.")
    
    return response.text


def get_united_masters_captcha_token(
    captcha_service: CapsolverService,
    proxy: Optional[str],
    cookies: List[dict],
    logger: SimpleLogger,
) -> str:
    
    settings_file_path = os.path.join(os.path.dirname(__file__), "united_master_captcha_settings.json")
    # print(f"Settings file path: {settings_file_path}")
    
    try:
        with open(settings_file_path, "r") as file:
            captcha_settings: TaskSettings = json.load(file)
    except FileNotFoundError:
        raise Exception(f"Settings file not found at path: {settings_file_path}")
    except json.JSONDecodeError as e:
        raise Exception(f"Error decoding JSON from settings file: {e}")
    


    logger.info("Loaded captcha settings:")
    # logger.info(f"Website Key: {captcha_settings.get('task').get('websiteKey')}")
    # logger.info(f"Website URL: {captcha_settings.get('task').get('websiteURL')}")
    # logger.info(f"Page Action: {captcha_settings.get('task').get('pageAction')}")
    # logger.info(f"Type: {captcha_settings.get('task').get('type')}")
    # logger.info(f"Cookies: {cookies}")
    # logger.info(f"Proxy: {proxy}")

    # if not captcha_settings.get("task").get("websiteKey"):
    #     raise Exception("Website Key is missing in captcha settings")
    # if not captcha_settings.get("task").get("websiteURL"):
    #     raise Exception("Website URL is missing in captcha settings")
    # if not captcha_settings.get("task").get("pageAction"):
    #     raise Exception("Page Action is missing in captcha settings")
    # if not captcha_settings.get("task").get("type"):
    #     raise Exception("Task type is missing in captcha settings")

    captcha_token = captcha_service.solve_captcha(
        website_key=captcha_settings.get('task').get("websiteKey"),
        website_url=captcha_settings.get('task').get("websiteURL"),
        page_action=captcha_settings.get('task').get("pageAction"),
        proxy=proxy,
        # "type": "ReCaptchaV3EnterpriseTaskProxyless",
        #  ReCaptchaV3Task
        type=captcha_settings.get('task').get("type"),
        cookies=cookies,
        anchor=captcha_settings.get('task').get("anchor"),
        reload=captcha_settings.get('task').get("reload"),
    )

    return captcha_token


def get_firebase_app_check_token(session: CurlCffiSession, recaptcha_token: str, logger: SimpleLogger):
    """
    Fetches the Firebase App Check token using the provided recaptcha token.

    Args:
        session: The Curl CFFI session to use for making the request.
        recaptcha_token (str): The recaptcha enterprise token.

    Returns:
        str: The Firebase App Check token.

    Raises:
        Exception: If the request fails or the response does not contain the expected token.
    """
    url = "https://content-firebaseappcheck.googleapis.com/v1/projects/um-prod/apps/1:191301842497:web:ce1fa5c46dfd19d7:exchangeRecaptchaEnterpriseToken?key=AIzaSyAk4hekTavR_VAVwjJ1vdIxjq1Dxn_3j48"

    payload = json.dumps({
        "recaptcha_enterprise_token": recaptcha_token
    })

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://unitedmasters.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://unitedmasters.com/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        # 'x-browser-channel': 'stable',
        # 'x-browser-copyright': 'Copyright 2025 Google LLC. All rights reserved.',
        # 'x-browser-validation': 'Hg4L+ikvx4e+Kz4C1Vi1rALvggw=',
        # 'x-browser-year': '2025',
        # 'x-client-data': 'CIi2yQEIprbJAQipncoBCNfeygEIk6HLAQiGoM0BGOHizgE='
    }

    response = session.request_with_retries(
        url=url,
        method="POST",
        data=payload,
        headers=headers,
        # proxies=get_residential_proxies(),
        ignore_status_codes=[403],
        impersonate="chrome",
        # debug=True,
    )

    print("Firebase App Check Status Code:", response.status_code)

    # # Save the response to a local file
    # with open("firebase_app_check_response.json", "w") as file:
    #     json.dump(response.text, file, indent=4)

    return response

