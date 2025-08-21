from botasaurus.browser import browser, Driver, Wait
from dotenv import load_dotenv
import os

from comcast_service import check_env_variables, get_and_print_cookies
from united_master_service import (
    click_a_button,
    handle_login,
    navigate_to_united_master,
)

load_dotenv()

check_env_variables()

@browser(profile="pikachu", proxy=os.getenv("RESIDENTIAL_PROXY"))
def login_to_united_master(driver: Driver, data):
    navigate_to_united_master(driver)

    click_a_button(
        driver, 'a[href="/login"]'
    )

    driver.long_random_sleep()

    handle_login(driver)

    driver.long_random_sleep()

    get_and_print_cookies(driver)

    driver.prompt("Final stop")

    return {}


# Initiate the web scraping task
login_to_united_master() # type: ignore
