import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging as logger

from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.assertions import Ensure
from ssqatest.homestory_assignment.pages.locators.SearchPageLocators import SearchPageLocators
from ssqatest.homestory_assignment.helpers.config_helpers import get_search_page_url


class SearchPage(SearchPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_there(self):
        logger.info("Navigating to Search page")
        url = get_search_page_url()
        self.driver.get(url)
        # Ensure.is_equal(self.driver.current_url, expected_url)

    def clear_input_search(self):
        logger.info("Clearing input search field")
        self.sl.wait_and_clear_input_field(self.INPUT_SEARCH)

    def enter_location_and_select_houston_tx(self, location):
        logger.info("Entering location and selecting value from dropdown suggestion")
        self.sl.enter_text_and_select_dropdown_suggestion(self.INPUT_SEARCH, location,
                                                          self.LOCATION_SUGGESTION_HOUSTON_TX)

    def find_all_listing_items(self):
        logger.info("Finding all list items")
        return self.sl.find_all_elements(self.LISTING_ITEMS, condition=EC.presence_of_all_elements_located)

    def verify_all_listings_have_price_in_range(self, min_price, max_price):
        logger.info("Finding all price elements")
        time.sleep(1)  # avoid finding listing elements with higher prices that are not disappeared yet with higher
        # prices
        price_elements = self.sl.find_all_elements(
            self.HOUSE_PRICE_ELEMENT, condition=EC.visibility_of_all_elements_located
        )

        prices_list = []
        for element in price_elements:
            price_text = self.driver.execute_script("""  
                let el = arguments[0];
                let child = el.querySelector('div');
                if (child) {
                    child.remove();
                }
                return el.textContent.trim();
            """, element)

            print("PRICE:", price_text)
            prices_list.append(price_text)

            # Removing dollar sign and comma in order to turn string into integer
            price_number = int(price_text.replace("$", "").replace(",", ""))
            prices_list.append(price_number)

            # Check if the price is between minimum and maximum
            Ensure.is_true(min_price <= price_number <= max_price,
                           f"Price {price_number} is out of range {min_price}-{max_price}")

        logger.info(f"All prices are within range {min_price}-{max_price}: {prices_list}")

    def click_price_button(self):
        logger.info("Clicking price")
        self.sl.wait_and_click(self.BUTTON_PRICE)

    def verify_that_price_range_element_is_visible(self):
        logger.info("Verifying that price dropdown is expanded")
        is_price_range_visible = self.sl.is_element_visible(self.SPAN_PRICE_RANGE)
        Ensure.is_true(is_price_range_visible)

    def verify_that_price_range_element_is_not_visible(self):
        logger.info("Verifying that price dropdown is collapsed")
        is_price_range_visible = self.sl.is_element_visible(self.SPAN_PRICE_RANGE)
        Ensure.is_false(is_price_range_visible)

    def enter_minimum_price(self, price_value):
        logger.info("Entering minimum price")
        self.sl.wait_and_enter_text(self.INPUT_MINIMUM_PRICE, price_value)
        self.sl.wait_and_click_key(self.INPUT_MINIMUM_PRICE, Keys.TAB)

    def enter_only_minimum_price(self, price_value):
        logger.info("Entering minimum price")
        self.sl.wait_and_enter_text(self.INPUT_MINIMUM_PRICE, price_value)
        self.sl.wait_and_click_key(self.INPUT_MINIMUM_PRICE, Keys.ENTER)

    def enter_maximum_price(self, price_value):
        logger.info("Entering maximum price")
        self.sl.wait_and_enter_text(self.INPUT_MAXIMUM_PRICE, price_value)
        self.sl.wait_and_click_key(self.INPUT_MAXIMUM_PRICE, Keys.ENTER)

    def wait_until_maximum_appears_in_price_button(self, text):
        logger.info(f"Waiting for '{text}' to appear..")
        self.sl.wait_until_element_contains_text(self.BUTTON_UP_TO_MAXIMUM, text)
        print(f"'{text}' text found in price button")

    def wait_until_minimum_appears_in_price_button(self, text):
        logger.info(f"Waiting for '{text}' to appear..")
        self.sl.wait_until_element_contains_text(self.BUTTON_FROM_MINIMUM, text)
        print(f"'{text}' text found in price button")
