import logging as logger

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.scopic_assignment.pages.locators.CheckoutPageLocators import CheckoutPageLocators


class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_you_are_on_checkout_page(self):
        logger.info("Verifying we are on 'Checkout page'")
        self.sl.wait_until_element_contains_text(self.CHECKOUT_PAGE_TITLE, "Checkout: Your Information")

    def enter_data_and_continue(self, first_name: str, last_name: str, postal_code: str):
        logger.info(f"Entering first name: {first_name}")
        self.sl.wait_and_enter_text(self.INPUT_FIRSTNAME, first_name)

        logger.info(f"Entering last name: {last_name}")
        self.sl.wait_and_enter_text(self.INPUT_LASTNAME, last_name)

        logger.info(f"Entering postal code: {postal_code}")
        self.sl.wait_and_enter_text(self.INPUT_POSTAL_CODE, postal_code)

        logger.info("Clicking continue..")
        self.sl.wait_and_click(self.BUTTON_CONTINUE)
