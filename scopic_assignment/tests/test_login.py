import pytest

from ssqatest.scopic_assignment.helpers.data_helpers import load_test_data
from ssqatest.scopic_assignment.pages.LoginPage import LoginPage
from ssqatest.scopic_assignment.pages.ProductsPage import ProductsPage
from ssqatest.src.helpers.assertions import Ensure


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.tcid300
    def test_verify_valid_user_login(self):
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)

        # extracting test data from external file
        users = load_test_data("users_data.json")
        valid_user = users["valid_user"]

        # login
        login_page.go_to_login_page()
        login_page.login(valid_user["username"], valid_user["password"])

        # verify user is logged in
        products_page.verify_that_you_are_on_the_products_page()

        # log out
        products_page.logout()
        login_page.verify_you_are_on_login_page()

    @pytest.mark.tcid301
    def test_verify_locked_out_user_cant_login(self):
        expected_error_message = "Epic sadface: Sorry, this user has been locked out."
        login_page = LoginPage(self.driver)

        # extracting test data from external file
        users = load_test_data("users_data.json")
        locked_out_user = users["locked_out_user"]

        # login
        login_page.go_to_login_page()
        login_page.login(locked_out_user["username"], locked_out_user["password"])

        # Verify error message is displayed for "locked_out" user
        login_page.verify_error_message_is_displayed(expected_error_message)

    @pytest.mark.tcid302
    def test_verify_user_cant_login_with_invalid_creds(self):
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"
        login_page = LoginPage(self.driver)

        # extracting test data from external file
        users = load_test_data("users_data.json")
        invalid_user = users["invalid_user"]

        # login
        login_page.go_to_login_page()
        login_page.login(invalid_user["username"], invalid_user["password"])

        # Verify error message is displayed for user with invalid username and password
        login_page.verify_error_message_is_displayed(expected_error_message)
