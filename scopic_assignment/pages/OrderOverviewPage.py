import logging as logger

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.scopic_assignment.pages.locators.OrderOverviewPageLocators import OrderOverviewPageLocators


class OrderOverviewPage(OrderOverviewPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_you_are_on_order_overview_page(self):
        logger.info("Verifying we are on 'Order Overview page'")
        self.sl.wait_until_element_contains_text(self.ORDER_OVERVIEW_PAGE_TITLE, "Checkout: Overview")

    def click_finish(self):
        logger.info("Clicking finish..")
        self.sl.wait_and_click(self.BUTTON_FINISH)

    def verify_order_confirmation_message_is_displayed(self):
        self.sl.wait_until_element_contains_text(self.ORDER_CONFIRMATION_MESSAGE, "Thank you for your order!")
        logger.info("Order confirmation message is displayed")
