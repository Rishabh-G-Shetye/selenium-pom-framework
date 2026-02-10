import time

from pages.login_page import LoginPage

def test_login(driver, base_url, credentials):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"], credentials["password"])
    time.sleep(2)
    assert "inventory" in driver.current_url, "Login failed - did not reach inventory page"