from selenium.webdriver.common.by import By

NAME_INPUT = (By.ID, 'name')
COMPANY_INPUT = (By.ID, 'company')
EMAIL_INPUT = (By.ID, 'email')
PASSWORD_INPUT = (By.ID, 'password')
CONFIRM_PASSWORD_INPUT = (By.ID, 'password-confirm')
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Register')]")

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*NAME_INPUT).clear()
        self.driver.find_element(*NAME_INPUT).send_keys(name)

    def enter_company(self, company):
        self.driver.find_element(*COMPANY_INPUT).clear()
        self.driver.find_element(*COMPANY_INPUT).send_keys(company)

    def enter_email(self, email):
        self.driver.find_element(*EMAIL_INPUT).clear()
        self.driver.find_element(*EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*PASSWORD_INPUT).clear()
        self.driver.find_element(*PASSWORD_INPUT).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(*CONFIRM_PASSWORD_INPUT).clear()
        self.driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)

    def click_register(self):
        self.driver.find_element(*REGISTER_BUTTON).click()

    def register(self, name, company, email, password, confirm_password):
        self.enter_name(name)
        self.enter_company(company)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_register()
