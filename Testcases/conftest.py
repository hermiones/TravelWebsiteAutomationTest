from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
from selenium import webdriver
import pytest
import os
from Utilities.ReadProperties import ReadConfig



@pytest.fixture(scope="session")
def driver():
    browser = ReadConfig.get_browser()
    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")  # Recommended for CI
        options.add_argument("--disable-dev-shm-usage")  # Recommended for CI
        options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # Avoid profile reuse issues

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    else:
        raise Exception(f"Browser {browser} not supported.")
    
    yield driver
    driver.quit()



Path_Screenshot = ReadConfig.get_screenshot_dir()


def save_ss(driver, filename):
    os.makedirs(Path_Screenshot, exist_ok=True)
    filepath = os.path.join(Path_Screenshot, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    driver.save_screenshot(filepath)
    return filepath


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            filename = f"FAIL_{item.name}.png"
            filepath = save_ss(driver, filename)
            try:
                import allure
                with open(filepath, "rb") as image_file:
                    allure.attach(image_file.read(), name=filename, attachment_type=allure.attachment_type.PNG)
            except ImportError:
                pass
