from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.PageCheckoutLocators import PageCheckoutLocators


class PageCheckout(PageCheckoutLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def select_country(self, country_name):
        self.sl.wait_and_select_dropdown_value(self.DROPDOWN_BILLING_COUNTRY, country_name)

    def enter_first_name(self, first_name):
        self.sl.wait_and_enter_text(self.INPUT_FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.sl.wait_and_enter_text(self.INPUT_LAST_NAME, last_name)

    def enter_street_address(self, street_name):
        self.sl.wait_and_enter_text(self.INPUT_STREET_ADDRESS, street_name)

    def enter_city(self, city):
        self.sl.wait_and_enter_text(self.INPUT_CITY, city)

    def enter_phone_number(self, phone_number):
        self.sl.wait_and_enter_text(self.INPUT_PHONE, phone_number)

    def enter_email(self, email_address):
        self.sl.wait_and_enter_text(self.INPUT_EMAIL, email_address)

    def enter_postal_code(self, postal_code):
        self.sl.wait_and_enter_text(self.INPUT_POSTAL_CODE, postal_code)

    def click_place_order(self):
        self.sl.wait_and_click(self.BUTTON_PLACE_ORDER)

