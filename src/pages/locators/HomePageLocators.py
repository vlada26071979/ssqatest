from selenium.webdriver.common.by import By


class HomePageLocators:

    BUTTON_CAP_ADD_TO_CART = (By.CSS_SELECTOR, "a[data-product_id='18']")
    LINK_VIEW_CART = (By.CSS_SELECTOR, "a[title='View cart']")

    PRODUCTS = (By.CSS_SELECTOR, "ul li.product")
    PAGE_HEADING = (By.CSS_SELECTOR, "h1.page-title")
    HEADERS = (By.CSS_SELECTOR, "ul.nav-menu li")
