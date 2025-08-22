import pytest
from selenium import webdriver
import os


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ["chrome", "firefox"]

    browser = os.environ.get("BROWSER")

    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Browser {browser} is not one of supported."
                        f"Supported are: {supported_browsers}")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver  # setting driver to a class variable
    yield
    driver.quit()
