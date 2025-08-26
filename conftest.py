import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def init_driver(request):
    chrome_options = Options()

    run_local = os.environ.get("GITHUB_ACTIONS", "false").lower() != "true"

    if not run_local:
        # Headless mode za CI
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    if run_local:
        driver.maximize_window()

    request.cls.driver = driver
    yield driver
    driver.quit()
