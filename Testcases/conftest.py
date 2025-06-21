import os
import pytest
from selenium import webdriver
from Utilities.ReadProperties import ReadConfig  # Adjust the import path as needed


@pytest.fixture(scope="session")
def driver():
    browser = ReadConfig.get_browser()
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
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
