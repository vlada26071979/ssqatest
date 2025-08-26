import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def init_driver(request):
    options = Options()

    run_local = os.environ.get("GITHUB_ACTIONS", "false").lower() != "true"

    if not run_local:
        # Headless mode za CI
        options.add_argument("--headless=new")  # headless mod
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    if run_local:
        driver.maximize_window()

    request.cls.driver = driver
    yield driver
    driver.quit()
