import random
import time
from capsolver_service import CapsolverService, SimpleLogger
from curl_cffi_session import createSession
from united_master_service import (
    get_firebase_app_check_token,
    get_residential_proxies,
    get_united_masters_captcha_token,
    visit_united_master_home_page,
)
import os
from dotenv import load_dotenv

load_dotenv()

logger = SimpleLogger()

"""
In this file we will try to get a fresh working captcha token using capsolver service 
and then use it to emulate the login process. The captcha token is used to get a working 
Firebase App Check token, which is important to send the first login request to this website.

NO SUCCESS YET, we are being detected

"""


api_key = os.getenv("CAPSOLVER_API_KEY")
if not api_key:
    raise Exception("CAPSOLVER_API_KEY is not set in the environment variables")

captcha_service = CapsolverService(api_key=api_key, logger=SimpleLogger())

session = createSession(
    logger=logger,
    # debug=True
)

try:
    visit_united_master_home_page(session, logger)

    # Convert session cookies to the required format: List[dict]
    cookies_list = [
        {"name": key, "value": value}
        for key, value in session.cookies.get_dict().items()
    ]

    while True:
        try:
            recaptcha_token = get_united_masters_captcha_token(
                captcha_service=captcha_service,
                cookies=cookies_list,
                proxy=None,
                # proxy=get_residential_proxies().get("http"),
                logger=logger,
            )

            print(f"Captcha Token: {recaptcha_token}")

            response = get_firebase_app_check_token(session, recaptcha_token, logger)

            if response.status_code != 403:
                logger.info("Firebase App Check Token Response:")
                logger.info(response.text)
                break  # Exit the loop if the response status is not 403
            else:
                # logger.warning(f"Received status code 403. Response: {response.status}")
                logger.warning("Retrying to fetch Firebase App Check Token...")

                # Add a small random delay between 1 and 3 seconds
                delay = random.uniform(1, 3)
                logger.info(
                    f"Adding a random delay of {delay:.2f} seconds before retrying..."
                )
                time.sleep(delay)
        except Exception as e:
            logger.error(f"Error occurred: {e}. Retrying...")

except Exception as e:
    print(f"Error occurred while fetching captcha token: {e}")
