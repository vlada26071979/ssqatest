import time
import pytest
from selenium.webdriver.common.by import By

from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.assertions import Ensure
from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.helpers.data_helpers import load_test_data
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_user(self):
        users = load_test_data("users.json")
        valid_user = users["valid_user"]

        my_account_page = MyAccountSignedOut(self.driver)
        my_acc_signed_in_page = MyAccountSignedIn(self.driver)

        my_account_page.go_to_my_account_page()
        my_account_page.enter_registration_email(valid_user["email"])
        my_account_page.enter_registration_password(valid_user["password"])
        my_account_page.click_register_button()
        my_acc_signed_in_page.wait_until_logout_link_is_displayed()

    @pytest.mark.tcid14
    def test_verify_you_can_not_register_existing_user(self):
        users = load_test_data("users.json")
        existing_user = users["existing_user"]

        expected_error_message = "An account is already registered with your email address"
        my_account_page = MyAccountSignedOut(self.driver)

        my_account_page.go_to_my_account_page()
        my_account_page.enter_registration_email(existing_user["email"])
        my_account_page.enter_registration_password(existing_user["password"])
        my_account_page.click_register_button()

        my_account_page.wait_until_user_already_registered_error_is_displayed(expected_error_message)
        time.sleep(5)

    @pytest.mark.tcid15
    def test_demo(self):
        my_account_page = MyAccountSignedOut(self.driver)

        my_account_page.go_to_my_account_page()
        Ensure.is_equal(self.driver.current_url, get_base_url() + my_account_page.endpoint)

        input_search = self.driver.find_element(By.ID, "woocommerce-product-search-field-0")
        Ensure.has_attribute(input_search, "placeholder", "Search products…")

