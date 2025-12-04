import logging as logger

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.scopic_assignment.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_you_are_on_cart_page(self):
        logger.info("Verifying we are on the 'Cart page'")
        self.sl.wait_until_element_contains_text(self.QUANTITY, "QTY")

    def continue_to_checkout_page(self):
        logger.info("Clicking Checkout")
        self.sl.wait_and_click(self.BUTTON_CHECKOUT)
