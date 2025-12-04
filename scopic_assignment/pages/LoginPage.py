import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging as logger

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.assertions import Ensure
from ssqatest.scopic_assignment.pages.locators.LoginPageLocators import LoginPageLocators
from ssqatest.scopic_assignment.helpers.config_helpers import get_login_page_url


class LoginPage(LoginPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_login_page(self):
        login_url = get_login_page_url()
        logger.info("Navigating to 'Login page'")
        self.driver.get(login_url)
        Ensure.is_equal(self.driver.current_url, login_url)

    def login(self, username: str, password: str):
        logger.info("Entering username")
        self.sl.wait_and_enter_text(self.INPUT_USERNAME, username)

        logger.info("Entering password")
        self.sl.wait_and_enter_text(self.INPUT_PASSWORD, password)

        logger.info("Clicking login button")
        self.sl.wait_and_click(self.BUTTON_LOGIN)

    def verify_error_message_is_displayed(self, expected_error_message):
        self.sl.wait_until_element_contains_text(self.ERROR_MESSAGE, expected_error_message)
        logger.info("Error message is displayed")

