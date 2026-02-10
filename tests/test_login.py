from pages.login_page import LoginPage

def test_login(driver):
    login = LoginPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")
