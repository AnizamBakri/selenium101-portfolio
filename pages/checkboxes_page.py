from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckboxesPage:

    URL = "https://the-internet.herokuapp.com/checkboxes"

    # All locators live here, not in the test
    CHECKBOXES = {
        1: (By.XPATH, "//form[@id='checkboxes']/input[1]"),
        2: (By.XPATH, "//form[@id='checkboxes']/input[2]")
    }        
        
    
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def load(self):
        self.driver.get(self.URL)
        return self
    
    def click_checkbox(self, box_num):
            
            checkbox= self.wait.until(EC.presence_of_element_located(self._get_locator(box_num)))
            checkbox.click()

    def get_checkbox_status(self, box_num):
        element = self.wait.until(EC.presence_of_element_located(self._get_locator(box_num)))
        return element.is_selected()

    def _get_locator(self, box_num):
        if box_num not in self.CHECKBOXES:
            raise ValueError(f"Checkbox {box_num} does not exist. Available: {list(self.CHECKBOXES.keys())}")
        return self.CHECKBOXES[box_num]