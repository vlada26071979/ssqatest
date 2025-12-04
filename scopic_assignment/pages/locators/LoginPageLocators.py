from selenium.webdriver.common.by import By


class LoginPageLocators:

    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[data-test='login-password']")
