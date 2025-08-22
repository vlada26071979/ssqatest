from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators


class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_logout_link_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.LOGOUT_LINK)
