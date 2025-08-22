import time
import pytest
from selenium.webdriver.common.by import By

from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_user(self):
        my_account_page = MyAccountSignedOut(self.driver)
        my_acc_signed_in_page = MyAccountSignedIn(self.driver)

        my_account_page.go_to_my_account_page()
        my_account_page.enter_registration_email("vlada2027@example.com")
        time.sleep(3)
        my_account_page.enter_registration_password("partizan2025!")
        time.sleep(2)
        my_account_page.click_register_button()
        my_acc_signed_in_page.wait_until_logout_link_is_displayed()
        breakpoint()

    def test_verify_you_can_not_register_existing_user(self):
        expected_error_message = "An account is already registered with your email address"
        my_account_page = MyAccountSignedOut(self.driver)

        my_account_page.go_to_my_account_page()

        my_account_page.enter_registration_email("vlada79@example.com")
        my_account_page.enter_registration_password("partizan2025!")
        my_account_page.click_register_button()

        my_account_page.wait_until_user_already_registered_error_is_displayed(expected_error_message)
        # message_element = self.driver.find_element(By.XPATH, '//li[contains(., "An account is already registered with your email address")]')
        # assert expected_error_message in message_element.text
        print("PASS")
