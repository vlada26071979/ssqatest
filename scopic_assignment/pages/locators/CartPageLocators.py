from selenium.webdriver.common.by import By


class CartPageLocators:

    QUANTITY = (By.CSS_SELECTOR, "[data-test='cart-quantity-label']")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "[data-test='checkout']")
