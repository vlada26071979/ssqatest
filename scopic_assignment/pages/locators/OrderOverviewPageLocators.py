from selenium.webdriver.common.by import By


class OrderOverviewPageLocators:

    ORDER_OVERVIEW_PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    BUTTON_FINISH = (By.CSS_SELECTOR, "[data-test='finish']")
    ORDER_CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "[data-test='complete-header']")