from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
import pytest


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
    login_page.login(ReadConfig.get_incorrect_email(), ReadConfig.get_incorrect_password())
    assert "You are logged in!" not in driver.page_source


# Blank email and password is provided
def test_log3(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login(ReadConfig.get_blank_email(), ReadConfig.get_blank_password())
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
    login_page.login(ReadConfig.get_username(), ReadConfig.get_incorrect_password())
    assert "You are logged in!" not in driver.page_source


# Unsuccessful login with blank username
def test_log6(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login(ReadConfig.get_blank_email(), ReadConfig.get_password())
    assert "You are logged in!" not in driver.page_source


# Unsuccessful login with valid email and wrong password
def test_log7_wrong_password(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login(ReadConfig.get_username(), "wrongpassword123")
    assert "You are logged in!" not in driver.page_source


# Login with long email and password
def test_log8_long_email_password(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    long_email = "a" * 256 + "@test.com"
    long_password = "p" * 256
    login_page.login(long_email, long_password)
    # Optionally, assert error message for long input


# Login with SQL injection attempt
def test_log9_sql_injection(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    sql_email = "' OR '1'='1"
    sql_password = "' OR '1'='1"
    login_page.login(sql_email, sql_password)
    assert "You are logged in!" not in driver.page_source


@pytest.mark.parametrize(
    "username,password,description",
    [
        (ReadConfig.get_login_valid_username(), ReadConfig.get_login_valid_password(), "Valid login"),
        (ReadConfig.get_login_invalid_username(), ReadConfig.get_login_invalid_password(), "Invalid login"),
        (ReadConfig.get_login_blank_username(), ReadConfig.get_login_blank_password(), "Blank credentials"),
        (ReadConfig.get_login_valid_username(), ReadConfig.get_login_invalid_password(), "Valid username, wrong password"),
        (ReadConfig.get_login_invalid_username(), ReadConfig.get_login_valid_password(), "Invalid username, valid password"),
        (ReadConfig.get_login_special_username(), ReadConfig.get_login_special_password(), "Special characters"),
        (ReadConfig.get_login_long_username(), ReadConfig.get_login_long_password(), "Long credentials"),
        (ReadConfig.get_login_valid_username(), ReadConfig.get_login_unicode_password(), "Unicode password"),
        (ReadConfig.get_login_valid_username(), ReadConfig.get_login_chinese_password(), "Chinese password"),
        (ReadConfig.get_login_valid_username(), ReadConfig.get_login_japanese_password(), "Japanese password"),
        (ReadConfig.get_login_valid_username(), ReadConfig.get_login_korean_password(), "Korean password"),
        (ReadConfig.get_login_sql_username(), ReadConfig.get_login_sql_password(), "SQL injection attempt"),
        (ReadConfig.get_login_xss_username(), ReadConfig.get_login_xss_password(), "XSS attempt"),
        # Add more combinations for 50+ cases as needed
    ]
)
def test_bulk_login_cases(driver, username, password, description):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    login_page = LoginPage(driver)
    login_page.login(username, password)
    # Optionally, assert login result based on 'description'
