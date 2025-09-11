import time

import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_non_existing_user(self):
        my_account_page = MyAccountSignedOut(self.driver)

        # go to my account
        my_account_page.go_to_my_account_page()
        my_account_page.enter_login_username("Vlada@gmail.com")
        my_account_page.enter_login_password("partizan")
        my_account_page.click_login_button()

        # verify error message
        expected_error_message = "Unknown email address. Check again or try your username."
        my_account_page.wait_until_error_is_displayed(expected_error_message)
