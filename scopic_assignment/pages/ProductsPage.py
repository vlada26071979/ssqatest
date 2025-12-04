import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging as logger

from ssqatest.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.support.select import Select
from ssqatest.src.helpers.assertions import Ensure
from ssqatest.scopic_assignment.pages.locators.ProductsPageLocators import ProductsPageLocators
from ssqatest.scopic_assignment.helpers.config_helpers import get_login_page_url


class ProductsPage(ProductsPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_that_you_are_on_the_products_page(self):
        self.sl.wait_until_element_contains_text(self.TITLE_PRODUCTS, "Products")
        logger.info("You have landed on the 'Products page'...")

    def filter_products(self, filter_option: str):
        logger.info(f"Selecting option {filter_option} from dropdown")
        filter_dropdown = self.sl.wait_until_element_is_visible(self.PRODUCT_SORT_DROPDOWN)
        select_object = Select(filter_dropdown)
        select_object.select_by_value(filter_option)

    def verify_correct_filter_is_selected(self, option: str):
        self.sl.wait_until_element_contains_text(self.PRODUCT_SORT_DROPDOWN, option)
        logger.info(f"Correct filter {option} has been selected")

    def add_product_to_cart(self, product_button):
        logger.info("Adding product to cart")
        self.sl.wait_and_click(product_button)

    def verify_cart_has_correct_number_of_products(self, products_number: str):
        logger.info(f"Verifying that cart has {products_number} product(s)")
        self.sl.wait_until_element_contains_text(self.SHOPPING_CART, products_number)
        logger.info(f"Cart has {products_number} products added")

    def click_cart(self):
        logger.info("Clicking cart..")
        self.sl.click_once_is_clickable(self.LINK_SHOPPING_CART)
