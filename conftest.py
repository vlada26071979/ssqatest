import os
import tempfile

from selenium import webdriver
from selenium.common import SessionNotCreatedException
from selenium.webdriver.chrome.options import Options
import pytest
from datetime import datetime


@pytest.fixture(scope="class")
def init_driver(request):
    options = Options()

    # Determine if it is local, Docker container or GitHub Actions run
    run_local = os.environ.get("GITHUB_ACTIONS", "false").lower() != "true"

    # you must set environmental variable DOCKER_RUN=TRUE on your local machine in order to this works correctly
    docker_run = os.environ.get("DOCKER_RUN", "false").lower() != "true"

    if not run_local or docker_run:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-background-timer-throttling")

        user_data_dir = tempfile.mkdtemp()  # this was added to avoid 'Session not created' issue
        options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = None
    for attempt in range(3):
        try:
            driver = webdriver.Chrome(options=options)
            break
        except SessionNotCreatedException as e:
            print(f"[WARNING] Chrome couldn't start (attempt {attempt + 1}/3): {e}")

    else:
        raise RuntimeError("Chrome WebDriver could not start after 3 attempts")

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
