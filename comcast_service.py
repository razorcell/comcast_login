import os
from botasaurus.browser import browser, Driver, Wait

def check_env_variables():
    required_envs = ["RESIDENTIAL_PROXY", "USERNAME", "PASSWORD"]
    for env in required_envs:
        value = os.getenv(env)
        if not value:
            raise Exception(f"{env} environment variable is not set or is empty.")
        print(f"{env} environment value: {value}")

def handle_cookies_accept(driver: Driver):
    try:
        driver.wait_for_element("#onetrust-accept-btn-handler", Wait.SHORT)
        if driver.select("#onetrust-accept-btn-handler"):
            driver.click("#onetrust-accept-btn-handler")
        else:
            print("No cookie accept button found.")
    except Exception as e:
        print(f"Exception occurred while handling cookies: {e}. This is acceptable if the accept button is not present.")


def navigate_to_comcast(driver: Driver):
    try:
        driver.google_get("https://business.comcast.com/")
        driver.short_random_sleep()
        print("Navigated to Comcast Business website.")
    except Exception as e:
        print(f"Error navigating to Comcast Business website: {e}")


def click_sign_in_button(driver: Driver, selector: str):
    try:
        driver.short_random_sleep()
        driver.wait_for_element(selector, Wait.SHORT)
        sign_in_button = driver.select(selector)
        if sign_in_button:
            print("Sign-in button found:", sign_in_button)
            driver.click(selector)
            print("Clicked the sign-in button.")
        else:
            print("Sign-in button not found.")
    except Exception as e:
        print(f"Error interacting with sign-in button: {e}")


def fill_input_field(driver: Driver, selector: str, value: str, field_name: str):
    try:
        input_element = driver.select(selector)
        if input_element:
            print(f"{field_name} input element found:", input_element)
            driver.type(selector, value, wait=Wait.SHORT)
            print(f"Typed {field_name} into the input field in a human-like manner.")
        else:
            print(f"{field_name} input element not found.")
    except Exception as e:
        print(f"Error filling {field_name} input field: {e}")


def handle_login(driver: Driver):
    username = os.getenv("USERNAME")
    if username:
        fill_input_field(driver, "input[id='user']", username, "USERNAME")
    else:
        print("USERNAME not found in environment variables.")

    driver.short_random_sleep()

    click_sign_in_button(driver, "#sign_in")

    driver.long_random_sleep()

    password = os.getenv("PASSWORD")
    if password:
        fill_input_field(driver, "input[id='passwd']", password, "PASSWORD")
    else:
        print("PASSWORD not found in environment variables.")

    driver.short_random_sleep()

    click_sign_in_button(driver, "#sign_in")

def show_balance(driver: Driver):
    try:
        balance_element = driver.select(
            "#cbs-billing-summary > div > div > div > div.bsd-billing-summary-details > div.bsd-billing-summary-balance-container > div > div:nth-child(1) > span.bsd-body-copy.bsd-body-copy--l.bsd-billing-summary-balance-item-value"
        )
        if balance_element:
            balance_text = driver.get_text(
                "#cbs-billing-summary > div > div > div > div.bsd-billing-summary-details > div.bsd-billing-summary-balance-container > div > div:nth-child(1) > span.bsd-body-copy.bsd-body-copy--l.bsd-billing-summary-balance-item-value"
            )
            print("Account Balance:", balance_text)
        else:
            print("Balance element not found.")
    except Exception as e:
        print(f"Error retrieving balance: {e}")

def get_and_print_cookies(driver: Driver):
    try:
        cookies = driver.get_cookies_dict()  # get the cookies from the driver
        if cookies:
            print("Cookies retrieved successfully:")
            for name, value in cookies.items():
                print(f"{name}: {value}")
        else:
            print("No cookies found.")
    except Exception as e:
        print(f"Error retrieving cookies: {e}")

