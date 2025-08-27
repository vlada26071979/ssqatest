import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from datetime import datetime


@pytest.fixture(scope="class")
def init_driver(request):
    options = Options()

    run_local = os.environ.get("GITHUB_ACTIONS", "false").lower() != "true"

    if not run_local:
        # Headless mode for GITHUB ACTIONS
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


@pytest.hookimpl(tryfirst=True, hookwrapper=False)
def pytest_runtest_makereport(item, call):
    """ Hook that creates screenshot only when test fails """

    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("init_driver")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "test_reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\nScreenshot saved to {file_path}")
