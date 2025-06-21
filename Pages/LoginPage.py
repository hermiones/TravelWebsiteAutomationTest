from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, 'email')  # Example: 'email' or 'username'
PASSWORD_INPUT = (By.ID, 'password')
LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*USERNAME_INPUT).clear()
        self.driver.find_element(*USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*PASSWORD_INPUT).clear()
        self.driver.find_element(*PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
