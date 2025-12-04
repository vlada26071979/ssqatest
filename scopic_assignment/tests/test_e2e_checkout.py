import pytest

from ssqatest.scopic_assignment.helpers.data_helpers import load_test_data
from ssqatest.scopic_assignment.pages.LoginPage import LoginPage
from ssqatest.scopic_assignment.pages.ProductsPage import ProductsPage
from ssqatest.scopic_assignment.pages.CartPage import CartPage
from ssqatest.scopic_assignment.pages.CheckoutPage import CheckoutPage
from ssqatest.scopic_assignment.pages.OrderOverviewPage import OrderOverviewPage


@pytest.mark.usefixtures("init_driver")
class TestCheckout:

    @pytest.mark.tcid303
    def test_verify_e2e_checkout(self):
        # instantiating page objects
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_overview_page = OrderOverviewPage(self.driver)

        # extracting test data from external file
        users = load_test_data("users_data.json")
        valid_user = users["valid_user"]

        # login
        login_page.go_to_login_page()
        login_page.login(valid_user["username"], valid_user["password"])

        # verify user is logged in
        products_page.verify_that_you_are_on_the_products_page()

        # Select high-to-low products filter
        products_page.filter_products("hilo")
        products_page.verify_correct_filter_is_selected("Price (high to low)")

        # adding first two products to cart
        products_page.add_product_to_cart(products_page.BUTTON_ADD_TO_CART_FLEECE_JACKET)
        products_page.add_product_to_cart(products_page.BUTTON_ADD_TO_CART_BACKPACK)

        # verifying we have 2 products added to cart
        products_page.verify_cart_has_correct_number_of_products("2")
        products_page.click_cart()

        # verifying we are on cart page and proceeding to checkout
        cart_page.verify_you_are_on_cart_page()
        cart_page.continue_to_checkout_page()

        # populate user data and continue
        checkout_page.verify_you_are_on_checkout_page()
        checkout_page.enter_data_and_continue("Vlada", "Djordjevic", "11000")

        # Completing order
        order_overview_page.verify_you_are_on_order_overview_page()
        order_overview_page.click_finish()
        order_overview_page.verify_order_confirmation_message_is_displayed()
