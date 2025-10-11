from selenium.webdriver.common.by import By


class SearchPageLocators:

    INPUT_SEARCH = (By.ID, "location_input")
    LOCATION_SUGGESTION_HOUSTON_TX = (By.XPATH, "//span[text()='Houston, TX']")
    LISTING_ITEMS = (By.CSS_SELECTOR, "div.listingItem__address___CKkGl")
    BUTTON_PRICE = (By.XPATH, "//button[contains(., 'Price')]")
    BUTTON_UP_TO_MAXIMUM = (By.XPATH, "//button[contains(., 'Up to $500K')]")
    BUTTON_FROM_MINIMUM = (By.XPATH, "//button[contains(., '$200K +')]")
    SPAN_PRICE_RANGE = (By.XPATH, "//span[text()='Price Range']")
    INPUT_MINIMUM_PRICE = (By.CSS_SELECTOR, "input.min_price_input__input")
    INPUT_MAXIMUM_PRICE = (By.CSS_SELECTOR, "input[aria-label='Maximum Price']")
    HOUSE_PRICE_ELEMENT = (By.CSS_SELECTOR, "div.listingItem__price___f8owm")






