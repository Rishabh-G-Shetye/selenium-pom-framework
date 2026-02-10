import os
from pickle import TRUE
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from screenshot_utility import take_screenshot

load_dotenv()

@pytest.fixture()
def driver():

    opts = Options()
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture()
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture()
def credentials():
    return {
        "username": os.getenv("SAUCE_USERNAME"),
        "password": os.getenv("SAUCE_PASSWORD")
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield()
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, f"Failed_{item.name}")