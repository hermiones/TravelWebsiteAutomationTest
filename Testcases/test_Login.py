from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig


# Successful login
def test_log1(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login(ReadConfig.get_username(), ReadConfig.get_password())
    # Optionally, assert successful login message
    # assert "You are logged in!" in driver.page_source
    driver.delete_all_cookies()


# Unsuccessful login
def test_log2(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login("incorrect@example.com", "incorrect_passwyyord")
    assert "You are logged in!" not in driver.page_source


# Blank email and password is provided
def test_log3(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login("", "")
    # Optionally, check for error message or alert
    # alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    # alert_text = alert.text
    # assert "Please fill in" in alert_text


# Test forgot password
def test_log4(driver):
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot Your Passwor").click()
    assert "Reset Password" in driver.page_source


# Unsuccessful login with wrong password
def test_log5(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login(ReadConfig.get_username(), "wrongpassword")
    assert "You are logged in!" not in driver.page_source


# Unsuccessful login with blank username
def test_log6(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login("", ReadConfig.get_password())
    assert "You are logged in!" not in driver.page_source


# Unsuccessful login with invalid email format
def test_log7(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login("invalidemail", ReadConfig.get_password())
    assert "You are logged in!" not in driver.page_source


# Unsuccessful login with blank password
def test_log8(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login("test@example.com", "")
    assert "You are logged in!" not in driver.page_source
