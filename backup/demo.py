from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Local driver fallback paths (edit these to your actual locations)
LOCAL_DRIVERS = {
    # "chrome": r"D:\drivers\chrome_driver\chromedriver.exe",
    # "firefox": r"D:\drivers\firefox_driver\geckodriver.exe",
    "edge": r"D:\projects\selenium_101_python\driver\msedgedriver.exe",
}

browsers = ["chrome", "firefox", "edge"]

for browser in browsers:
    print(f"\n--- Testing on {browser.upper()} ---")

    driver = None
    try:
        # Try using WebDriverManager first
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            print(f"Unknown browser: {browser}")
            continue

        driver.get("https://www.wikipedia.org/")
        print("Title 1:", driver.title)
        
        # Example interaction: Click on the language selection button
        wait = WebDriverWait(driver, 10)
        lang_button = wait.until(EC.element_to_be_clickable((By.ID, "js-lang-list-button")))
        lang_button.click()

        malay_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[lang="ms"]')))
        malay_link.click()
        print("Navigated to:", driver.current_url)
        wait.until(EC.title_contains("Wikipedia"))
        print("Title 2:", driver.title)

    except Exception as e:
        print(f"Something went wrong:\nError message: {e}\nError type: {type(e)}")
        print(f"Trying local driver for {browser}...")

        try:
            # Fallback to local driver
            if browser == "chrome":
                driver = webdriver.Chrome(service=ChromeService(LOCAL_DRIVERS["chrome"]))
            elif browser == "firefox":
                driver = webdriver.Firefox(service=FirefoxService(LOCAL_DRIVERS["firefox"]))
            elif browser == "edge":
                driver = webdriver.Edge(service=EdgeService(LOCAL_DRIVERS["edge"]))

            driver.get("https://www.wikipedia.org/")
            print("Title:", driver.title)

            # Example interaction: Click on the language selection button
            wait = WebDriverWait(driver, 10)
            lang_button = wait.until(EC.element_to_be_clickable((By.ID, "js-lang-list-button")))
            lang_button.click()

            malay_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[lang="ms"]')))
            malay_link.click()
            print("Navigated to:", driver.current_url)
            wait.until(EC.title_contains("Wikipedia"))
            print("Title 2:", driver.title)

        except Exception as e2:
            print(f"Local driver for {browser} also failed: {e2}")

    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass