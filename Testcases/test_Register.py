from selenium.webdriver.common.by import By
from Utilities.ReadProperties import ReadConfig


# Validating the title of the webpage
def test_reg1(driver):
    driver.get(ReadConfig.get_base_url())
    assert driver.title == "BlazeDemo"

# Navigating to the homepage
def test_reg2(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

# Navigating to the Registration page and registering as a user with valid credentials
def test_reg3(driver):
    driver.get(ReadConfig.get_base_url())
    driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
    driver.find_element(By.ID, "name").send_keys(ReadConfig.get_username())
    driver.find_element(By.ID, "company").send_keys("ABC Corp")
    driver.find_element(By.ID, "email").send_keys(ReadConfig.get_username())
    driver.find_element(By.ID, "password").send_keys(ReadConfig.get_password())
    driver.find_element(By.ID, "password-confirm").send_keys(ReadConfig.get_password())
    driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").click()

