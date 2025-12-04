from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    CHECKOUT_PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    INPUT_POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")

    BUTTON_CONTINUE = (By.CSS_SELECTOR, "[data-test='continue']")



