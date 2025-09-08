import pytest

from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.data_helpers import load_test_data
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_user(self):
        email, password = generate_random_email_and_password()

        my_account_page_signed_out = MyAccountSignedOut(self.driver)
        my_acc_signed_in_page = MyAccountSignedIn(self.driver)

        my_account_page_signed_out.go_to_my_account_page()
        my_account_page_signed_out.enter_registration_email(email)
        my_account_page_signed_out.enter_registration_password(password)
        my_account_page_signed_out.click_register_button()
        my_acc_signed_in_page.wait_until_logout_link_is_displayed()

    @pytest.mark.tcid14
    def test_verify_you_can_not_register_existing_user(self):
        users = load_test_data("users.json")
        existing_user = users["existing_user"]

        expected_error_message = "An account is already registered with your email address"
        my_account_page_signed_out = MyAccountSignedOut(self.driver)

        my_account_page_signed_out.go_to_my_account_page()
        my_account_page_signed_out.enter_registration_email(existing_user["email"])
        my_account_page_signed_out.enter_registration_password(existing_user["password"])
        my_account_page_signed_out.click_register_button()

        my_account_page_signed_out.wait_until_user_already_registered_error_is_displayed(expected_error_message)
