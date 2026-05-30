from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "https://the-internet.herokuapp.com/login"

    # All locators live here, not in the test
    FLASH_TEXT  = (By.ID, "flash")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    USERNAME_FORM = (By.ID, "username")
    PASSWORD_FORM = (By.ID, "password")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def load(self):
        self.driver.get(self.URL)
        return self

    def fill_login_form(self, username, password):
        username_field = self.wait.until(EC.presence_of_element_located(self.USERNAME_FORM))
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FORM))
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()
        return self
    
    def get_flash_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FLASH_TEXT))
        return element.text