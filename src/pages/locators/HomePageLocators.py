from selenium.webdriver.common.by import By


class HomePageLocators:

    BUTTON_CAP_ADD_TO_CART = (By.CSS_SELECTOR, "a[data-product_id='18']")
    LINK_VIEW_CART = (By.CSS_SELECTOR, "a[title='View cart']")