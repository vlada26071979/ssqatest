import time

import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.HeaderPagePart import HeaderPagePart
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.PageCheckout import PageCheckout
from ssqatest.src.pages.PageOrderReceived import PageOrderReceived
from ssqatest.src.pages.locators.PageCheckoutLocators import PageCheckoutLocators
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        cart_page = CartPage(self.driver)
        page_checkout = PageCheckout(self.driver)
        page_order_received = PageOrderReceived(self.driver)

        # go to home page
        home_page.go_to_home_page()

        # add 1 item to cart and go to cart
        home_page.scroll_to_button_cap_add_to_cart()
        home_page.add_cap_to_cart()

        # Apply free coupon SSQA100
        cart_page.enter_coupon_code("SSQA100")
        cart_page.click_apply_coupon()
        cart_page.verify_that_coupon_is_applied_successfully()

        # select free shipping
        cart_page.select_free_shipping()

        # click on proceed to checkout
        cart_page.click_proceed_to_checkout()

        # fill in the form
        page_checkout.enter_first_name("Vlada")
        page_checkout.enter_last_name("Djordjevic")
        page_checkout.select_country(country_name="RS")
        page_checkout.enter_street_address("Krajiskih brigada 13")
        page_checkout.enter_city("Belgrade")
        page_checkout.enter_postal_code("11000")
        page_checkout.enter_phone_number(888111223)
        page_checkout.enter_email("vlada79@partizan.com")

        # click on place order
        page_checkout.click_place_order()

        # verify order is successfully placed
        page_order_received.verify_order_is_placed_successfully()
        order_number = page_order_received.get_order_number()
        print(f"Order number {order_number} successfully placed")
