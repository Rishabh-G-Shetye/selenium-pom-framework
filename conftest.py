import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

@pytest.fixture()
def driver():

    opts = Options()
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.paaaword_manager_leak_detection": False
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
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
