from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderPagePartLocators import HeaderPagePartLocators


class HeaderPagePart(HeaderPagePartLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_cart_link(self):
        self.sl.wait_and_click(self.LINK_CART)
