from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, timeout=10)

# Defensive wait — harmless on static elements, essential on dynamic ones
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
button.click()

wait = WebDriverWait(driver, timeout=10)
element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

print(element.text)

driver.quit()