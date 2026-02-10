from pages.login_page import LoginPage

def test_login(driver, base_url, credentials):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(credentials["username"], credentials["password"])
