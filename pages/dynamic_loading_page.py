from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicLoadingPage:

    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    # All locators live here, not in the test
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT  = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def load(self):
        self.driver.get(self.URL)
        return self        # lets you chain: page.load().click_start()

    def click_start(self):
        button = self.wait.until(EC.element_to_be_clickable(self.START_BUTTON))
        button.click()
        return self

    def get_finish_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FINISH_TEXT))
        return element.text