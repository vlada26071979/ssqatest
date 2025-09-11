import datetime
import time

from selenium.common import TimeoutException, StaleElementReferenceException, UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class SeleniumExtended:

    def __init__(self, driver):
        """
        Initialize the extended Selenium wrapper.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.default_wait_secs = 10

    def _wait(self, wait_secs=20):
        """
        Create a WebDriverWait instance.

        :param wait_secs: Maximum wait time in seconds
        :return: WebDriverWait instance
        """
        return WebDriverWait(self.driver, wait_secs)

    def wait_and_enter_text(self, locator, text):
        """
        Wait until the element is visible and enter the provided text.

        :param locator: Locator tuple for the element
        :param text: Text to enter into the element
        """
        self._wait().until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click(self, locator):
        """
        Wait until the element is visible and click on it.

        :param locator: Locator tuple for the element
        """
        self._wait().until(EC.visibility_of_element_located(locator)).click()

    def click_once_is_clickable(self, locator):
        """
        Wait until the element is clickable and click on it.

        :param locator: Locator tuple for the element
        """
        self._wait().until(EC.element_to_be_clickable(locator)).click()

    def wait_until_element_contains_text(self, locator, text, wait_secs=None):
        """
        Wait until the element contains the specified text.

        :param locator: Locator tuple for the element
        :param text: Text expected to be present in the element
        :param wait_secs: Optional custom wait time
        """
        self._wait(wait_secs or self.default_wait_secs).until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_element_is_visible(self, locator):
        """
        Wait until the element is visible and return it.

        :param locator: Locator tuple for the element
        :return: WebElement once visible
        """
        element = self._wait().until(EC.visibility_of_element_located(locator))
        print("Element is visible on the page")
        return element

    def is_element_visible(self, locator, timeout=None):
        """
        Check if an element is visible within the specified timeout.

        :param locator: Locator tuple for the element
        :param timeout: Optional custom wait time
        :return: True if element is visible, False otherwise
        """
        try:
            self._wait(timeout or self.default_wait_secs).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_and_scroll_to_element(self, locator):
        """
        Wait until the element is visible and scroll it into view.

        :param locator: Locator tuple for the element
        """
        element = self._wait().until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def wait_and_select_dropdown_value(self, dropdown_locator, value):
        """
        Wait until the dropdown is visible and select an option by value.

        :param dropdown_locator: Locator tuple for the dropdown element
        :param value: Value to select in the dropdown
        """
        dropdown = self._wait().until(EC.visibility_of_element_located(dropdown_locator))
        dropdown = Select(dropdown)
        dropdown.select_by_value(value)

    def find_element(self, locator, condition=EC.presence_of_element_located, wait_secs=10):
        """
        Find a web element with retry logic and exception handling.

        :param locator: Locator tuple for the element
        :param condition: Expected condition to wait for (default: presence_of_element_located)
        :param wait_secs: Maximum wait time in seconds
        :return: WebElement
        :raises TimeoutException: If element not found in time
        :raises Exception: For unexpected errors
        """
        start_time = datetime.datetime.now()
        while datetime.datetime.now() - start_time < datetime.timedelta(seconds=wait_secs):
            try:
                return self._wait().until(condition(locator))

            except StaleElementReferenceException:
                print(f"[INFO] Retrying due to StaleElementReferenceException for locator: {locator}")

            except TimeoutException as e:
                msg = str(e).strip()
                if msg in ("", "Message:"):
                    raise TimeoutException(f"[ERROR] Element {locator} was not found within {wait_secs} seconds")
                else:
                    raise

            except UnexpectedAlertPresentException:
                print("[INFO] Unexpected alert detected – consider adding a handler here")

            time.sleep(0.1)

        raise Exception(f"[ERROR] find_element failed: {locator} was not found within {wait_secs} seconds")

    def wait_and_get_text(self, locator):
        """
        Wait until the element is visible and return its text content.

        :param locator: Locator tuple for the element
        :return: Text content of the element
        :raises TimeoutException: If the element is not visible within the specified timeout - 20scs by default
        """

        element = self._wait().until(EC.visibility_of_element_located(locator))
        element_text = element.text

        return element_text

    def click_with_js(self, locator):
        """
         Click on an element using JavaScript.

         :param locator: Locator tuple for the element
         :return: None
         :raises TimeoutException: If the element cannot be found within the specified timeout
         """

        element = self.find_element(locator)
        self.driver.execute_script("return arguments[0].click();", element)

    def find_all_elements(self, locator):
        """
          Find and return all elements matching the given locator.

          :param locator: Locator tuple for the elements
          :return: List of WebElement objects
          :raises TimeoutException: If no elements are visible within the specified timeout
          """
        return self._wait().until(EC.visibility_of_all_elements_located(locator))

