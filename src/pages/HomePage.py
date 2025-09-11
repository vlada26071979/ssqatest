from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_page_url = get_base_url()
        self.driver.get(home_page_url)

    def add_cap_to_cart(self):
        self.sl.wait_and_click(self.BUTTON_CAP_ADD_TO_CART)
        self.sl.wait_and_click(self.LINK_VIEW_CART)

    def scroll_to_button_cap_add_to_cart(self):
        self.sl.wait_and_scroll_to_element(self.BUTTON_CAP_ADD_TO_CART)

    def get_all_product_elements(self):
        all_products = self.sl.find_all_elements(self.PRODUCTS)
        return all_products

    def get_displayed_heading(self):
        return self.sl.wait_and_get_text(self.PAGE_HEADING)
