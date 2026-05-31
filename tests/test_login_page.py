import pytest
from pages.login_page import LoginPage as lp

# def test_valid_login(driver):
#     username = "tomsmith"
#     password = "SuperSecretPassword!"

#     page = lp(driver)
#     page.load().fill_login_form(username,password).click_login()
#     assert "You logged into a secure area!" in page.get_flash_text()
#     #assert "WRONG TEXT" in page.get_flash_text()

# def test_invalid_login(driver):
#     username = "wrongusername"
#     password = "wrongpassword"

#     page = lp(driver)
#     page.load().fill_login_form(username,password).click_login()
#     assert "Your username is invalid!" in page.get_flash_text()

@pytest.mark.parametrize("username,password,error_message", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("wrongusername", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrongpassword", "Your password is invalid!"),
    ("wrongusername", "wrongpassword", "Your username is invalid!"),
    ("", "", "Your username is invalid!")
])

def test_login(driver, username, password, error_message):
    page = lp(driver)
    page.load().fill_login_form(username,password).click_login()
    assert error_message in page.get_flash_text()