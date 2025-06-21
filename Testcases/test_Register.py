from selenium.webdriver.common.by import By
from Utilities.ReadProperties import ReadConfig
from Pages.RegisterPage import RegisterPage


# Validating the title of the webpage
def test_reg1(driver):
    driver.get(ReadConfig.get_base_url())
    assert driver.title == "BlazeDemo"


# Navigating to the homepage
def test_reg2(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()


# Register with valid credentials
def test_reg3(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    reg_page = RegisterPage(driver)
    reg_page.register(
        ReadConfig.get_username(),
        "ABC Corp",
        ReadConfig.get_username(),
        ReadConfig.get_password(),
        ReadConfig.get_password(),
    )


# Registration with blank fields
def test_reg4_blank_fields(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    reg_page = RegisterPage(driver)
    reg_page.register(
        ReadConfig.get_blank_email(),
        "",
        ReadConfig.get_blank_email(),
        ReadConfig.get_blank_password(),
        ReadConfig.get_blank_password(),
    )
    # Optionally, assert error message


# Registration with mismatched passwords
def test_reg5_mismatched_passwords(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    reg_page = RegisterPage(driver)
    reg_page.register(
        ReadConfig.get_incorrect_email(),
        "Test Company",
        ReadConfig.get_incorrect_email(),
        ReadConfig.get_password(),
        ReadConfig.get_incorrect_password(),
    )
    # Optionally, assert error message for password mismatch


# Registration with invalid email
def test_reg6_invalid_email(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    reg_page = RegisterPage(driver)
    reg_page.register(
        ReadConfig.get_invalid_email(),
        "Test Company",
        ReadConfig.get_invalid_email(),
        ReadConfig.get_password(),
        ReadConfig.get_password(),
    )
    # Optionally, assert error message for invalid email


# Registration with already registered email
def test_reg7_existing_email(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    reg_page = RegisterPage(driver)
    reg_page.register(
        ReadConfig.get_username(),
        "Test Company",
        ReadConfig.get_username(),
        ReadConfig.get_password(),
        ReadConfig.get_password(),
    )
    # Optionally, assert error message for existing email

