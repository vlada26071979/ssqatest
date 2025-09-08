from selenium.webdriver.common.by import By


class CartPageLocators:
    INPUT_COUPON_CODE = (By.ID, "coupon_code")
    BUTTON_APPLY_COUPON = (By.NAME, "apply_coupon")
    INPUT_FREE_SHIPPING = (By.ID, "shipping_method_0_free_shipping3")

    COUPON_APPLIED_SUCCESSFULLY_ELEMENT = (By.CSS_SELECTOR, "div.woocommerce-message")
    BUTTON_PROCEED_TO_CHECKOUT = (By.XPATH, '//a[normalize-space(text())="Proceed to checkout"]')
