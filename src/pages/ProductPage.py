from ssqatest.src.pages.locators.ProductPageLocators import ProductPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended

class ProductPage(ProductPageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_displayed_product_name(self):
        return self.sl.wait_and_get_text(self.PRODUCT_TITLE)

