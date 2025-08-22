from selenium.webdriver.common.by import By


class MyAccountSignedOutLocators:

    LOGIN_USERNAME_FIELD = (By.ID, "username")
    LOGIN_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")

    ERROR_UL = (By.CSS_SELECTOR, "ul.woocommerce-error")

    REGISTRATION_EMAIL_FIELD = (By.ID, "reg_email")
    REGISTRATION_PASSWORD_FIELD = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")

    ALREADY_REGISTERED_ERROR_ELEMENT = (By.XPATH, '//li[contains(., "An account is already registered with your email address")]')
