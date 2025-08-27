from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_wait_secs = 10

    def _wait(self, wait_secs=20):
        return WebDriverWait(self.driver, wait_secs)

    # def wait_and_enter_text(self, locator, text, wait_secs=None):
    #     wait_secs = wait_secs if wait_secs else self.default_wait_secs
    #     WebDriverWait(self.driver, wait_secs).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_enter_text(self, locator, text):
        self._wait().until(EC.visibility_of_element_located(locator)).send_keys(text)

    # def wait_and_click(self, locator, wait_secs=None):
    #     wait_secs = wait_secs if wait_secs else self.default_wait_secs
    #     WebDriverWait(self.driver, wait_secs).until(EC.visibility_of_element_located(locator)).click()

    def wait_and_click(self, locator):
        self._wait().until(EC.visibility_of_element_located(locator)).click()

    def click_once_is_clickable(self, locator):
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    # def wait_until_element_contains_text(self, locator, text, wait_secs=None):
    #     wait_secs = wait_secs if wait_secs else self.default_wait_secs
    #     WebDriverWait(self.driver, wait_secs).until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_contains_text(self, locator, text, wait_secs=None):
        self._wait().until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_is_visible(self, locator):
        element = self._wait().until(EC.visibility_of_element_located(locator))
        print("Element is visible on the page")
        return element

    def is_element_visible(self, locator, timeout=None):
        """Returns True if element is visible, otherwise False"""
        try:
            self._wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
