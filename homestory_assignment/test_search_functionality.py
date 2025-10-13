import pytest
import logging as logger

from ssqatest.src.helpers.assertions import Ensure
from ssqatest.homestory_assignment.pages.SearchPage import SearchPage


@pytest.mark.usefixtures("init_driver")
class TestSearchFunctionality:

    @pytest.mark.tcid500
    def test_verify_location_search_results(self):
        location = "Houston, TX"
        expected_listing_items_number = 50  # there are 50 listing items on the page
        search_page = SearchPage(self.driver)

        search_page.go_there()
        breakpoint()  # Solve CAPTCHA manually if appears

        search_page.clear_input_search()
        search_page.enter_location_and_select_houston_tx(location)

        listing_items = search_page.find_all_listing_items()
        Ensure.is_equal(len(listing_items), expected_listing_items_number)

        for index, item in enumerate(listing_items):
            Ensure.is_in(location, item.text)  # making sure that every list item contains text "Houston, TX"
            logger.info(f"List item number {index + 1} contains expected text")

    @pytest.mark.tcid501
    def test_verify_price_dropdown_expands_and_collapses_correctly(self):
        location = "Houston, TX"
        search_page = SearchPage(self.driver)

        search_page.go_there()
        breakpoint()  # Solve CAPTCHA manually if appears

        search_page.clear_input_search()
        search_page.enter_location_and_select_houston_tx(location)

        search_page.click_price_button()
        search_page.verify_that_price_range_element_is_visible()  # making sure that price button is expanded
        search_page.click_price_button()
        search_page.verify_that_price_range_element_is_not_visible()  # making sure that price button is collapsed

    @pytest.mark.tcid502
    def test_verify_price_range_filter_displays_correct_results(self):
        location = "Houston, TX"
        minimum_price = "$200,000"
        maximum_price = "$300,000"
        search_page = SearchPage(self.driver)

        search_page.go_there()
        breakpoint()  # Solve CAPTCHA manually if appears

        search_page.clear_input_search()
        search_page.enter_location_and_select_houston_tx(location)

        search_page.click_price_button()
        search_page.enter_minimum_price(minimum_price)
        search_page.enter_maximum_price(maximum_price)
        search_page.verify_all_listings_have_price_in_range(200000, 300000)

    @pytest.mark.tcid503
    def test_verify_price_range_filter_with_no_maximum(self):
        location = "Houston, TX"
        minimum_price = "$200,000"
        expected_text = "$200K +"
        search_page = SearchPage(self.driver)

        search_page.go_there()
        breakpoint()  # Solve CAPTCHA manually if appears

        search_page.clear_input_search()
        search_page.enter_location_and_select_houston_tx(location)

        search_page.click_price_button()
        search_page.enter_only_minimum_price(minimum_price)
        search_page.wait_until_minimum_appears_in_price_button(expected_text)

    @pytest.mark.tcid504
    def test_verify_price_range_filter_with_no_minimum(self):
        location = "Houston, TX"
        maximum_price = "$500,000"
        expected_text = "Up to $500K"
        search_page = SearchPage(self.driver)

        search_page.go_there()
        breakpoint()  # Solve CAPTCHA manually if appears and then continue test execution

        search_page.clear_input_search()
        search_page.enter_location_and_select_houston_tx(location)

        search_page.click_price_button()
        search_page.enter_maximum_price(maximum_price)
        search_page.wait_until_maximum_appears_in_price_button(expected_text)
