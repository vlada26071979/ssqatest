from selenium.webdriver.common.by import By


class PageCheckoutLocators:
    INPUT_FIRST_NAME = (By.ID, "billing_first_name")
    INPUT_LAST_NAME = (By.ID, "billing_last_name")

    DROPDOWN_BILLING_COUNTRY = (By.ID, "billing_country")
    INPUT_STREET_ADDRESS = (By.ID, "billing_address_1")
    INPUT_CITY = (By.ID, "billing_city")
    INPUT_POSTAL_CODE = (By.ID, "billing_postcode")
    INPUT_PHONE = (By.ID, "billing_phone")
    INPUT_EMAIL = (By.ID, "billing_email")

    BUTTON_PLACE_ORDER = (By.ID, "place_order")
