from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocators):
    endpoint = "/my-account/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account_page(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to url: {my_account_url}")
        self.driver.get(my_account_url)

    def enter_login_username(self, username):
        logger.info("Enter username")
        self.sl.wait_and_enter_text(self.LOGIN_USERNAME_FIELD, username)

    def enter_login_password(self, password):
        logger.info("Enter password")
        self.sl.wait_and_enter_text(self.LOGIN_PASSWORD_FIELD, password)

    def enter_registration_email(self, email):
        self.sl.wait_and_enter_text(self.REGISTRATION_EMAIL_FIELD, email)

    def enter_registration_password(self, password):
        self.sl.wait_and_enter_text(self.REGISTRATION_PASSWORD_FIELD, password)

    def click_register_button(self):
        self.sl.click_once_is_clickable(self.REGISTER_BUTTON)

    def click_login_button(self):
        logger.info("Clicking login button")
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, expected_error_message):
        self.sl.wait_until_element_contains_text(self.ERROR_UL, expected_error_message)

    def wait_until_user_already_registered_error_is_displayed(self, expected_error_message):
        self.sl.wait_until_element_contains_text(self.ALREADY_REGISTERED_ERROR_ELEMENT, expected_error_message)

