from botasaurus.browser import browser, Driver, Wait
from dotenv import load_dotenv
import os

from comcast_service import (
    check_env_variables,
    click_sign_in_button,
    get_and_print_cookies,
    handle_cookies_accept,
    handle_login,
    navigate_to_comcast,
    show_balance,
)

load_dotenv()

check_env_variables()


@browser(profile="pikachu", proxy=os.getenv("RESIDENTIAL_PROXY"))
def login_to_comcast(driver: Driver, data):
    navigate_to_comcast(driver)

    handle_cookies_accept(driver)

    click_sign_in_button(
        driver, "#bcp-header > nav.bsd-nav-l1 > div.bsd-l1-right-nav > a > span"
    )

    driver.long_random_sleep()

    handle_cookies_accept(driver)

    handle_login(driver)

    driver.long_random_sleep()

    show_balance(driver)

    get_and_print_cookies(driver)

    driver.prompt("Final stop")

    return {}


# Initiate the web scraping task
login_to_comcast()
