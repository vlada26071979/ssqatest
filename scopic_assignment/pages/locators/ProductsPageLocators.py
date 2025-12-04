from selenium.webdriver.common.by import By


class ProductsPageLocators:
    TITLE_PRODUCTS = (By.CSS_SELECTOR, "span[data-test='title']")
    PRODUCT_SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")

    BUTTON_ADD_TO_CART_FLEECE_JACKET = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-fleece-jacket']")
    BUTTON_ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")

    SHOPPING_CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    LINK_SHOPPING_CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
