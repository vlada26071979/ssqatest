import random
import string
import logging as logger
import os
from datetime import datetime


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = "partizan.com"
    if not email_prefix:
        email_prefix = "testuser"

    random_email_length = 10
    random_string = "".join(random.choices(string.ascii_lowercase, k=random_email_length))

    email = email_prefix + "" + random_string + "@" + domain

    logger.info(f"Generated random email: {email}")

    random_password_length = 20
    password = "".join(random.choices(string.ascii_letters, k=random_password_length))

    return email, password


def take_screenshot(driver, step_name="step"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshots_dir = "test_reports/screenshots"

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    filename = os.path.join(screenshots_dir, f"{timestamp}_{step_name}.png")
    driver.save_screenshot(filename)
    print(f"[INFO] Screenshot saved: {filename}")
