import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# pytest hook — runs automatically after every test
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield                        # run the test
    report = outcome.get_result()

    # only care about the actual test call, not setup/teardown
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")   # get the driver from the test
        if driver:
            # create screenshots folder if it doesn't exist
            os.makedirs("screenshots", exist_ok=True)
            # name the file after the test that failed
            filename = f"screenshots/{item.name}.png"
            driver.save_screenshot(filename)
            print(f"\nScreenshot saved: {filename}")