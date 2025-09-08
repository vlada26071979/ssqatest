from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def enter_coupon_code(self, coupon_code):
        self.sl.wait_and_enter_text(self.INPUT_COUPON_CODE, coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.BUTTON_APPLY_COUPON)

    def click_proceed_to_checkout(self):
        self.sl.wait_until_element_is_visible(self.BUTTON_PROCEED_TO_CHECKOUT)
        self.sl.click_with_js(self.BUTTON_PROCEED_TO_CHECKOUT)

    def select_free_shipping(self):
        self.sl.wait_until_element_is_visible(self.INPUT_FREE_SHIPPING)
        self.sl.click_with_js(self.INPUT_FREE_SHIPPING)

    def verify_that_coupon_is_applied_successfully(self, text="Coupon code applied successfully."):
        self.sl.wait_until_element_contains_text(self.COUPON_APPLIED_SUCCESSFULLY_ELEMENT, text)
