from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Locators for the flight booking page
DEPARTURE_DROPDOWN = (By.XPATH, "/html[1]/body[1]/div[3]/form[1]/select[1]")
DESTINATION_DROPDOWN = (By.XPATH, "/html[1]/body[1]/div[3]/form[1]/select[2]")
FIND_FLIGHTS_BUTTON = (By.XPATH, "/html[1]/body[1]/div[3]/form[1]/div[1]/input[1]")
CHOOSE_FLIGHT_BUTTON = (By.XPATH, "/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/input[1]")
INPUT_NAME = (By.ID, "inputName")
INPUT_ADDRESS = (By.ID, "address")
INPUT_CITY = (By.ID, "city")
PURCHASE_BUTTON = (By.XPATH, "/html[1]/body[1]/div[2]/form[1]/div[11]/div[1]/input[1]")
DEST_WEEK_LINK = (By.XPATH, "//a[normalize-space()='destination of the week! The Beach!']")
LUFTHANSA_CELL = (By.XPATH, "//td[normalize-space()='Lufthansa']")
SELECT_AIRLINE_BUTTON = (By.XPATH, "//tbody/tr[5]/td[1]/input[1]")

class FlightBookingPage:
    def __init__(self, driver):
        self.driver = driver

    def select_departure(self, city):
        Select(self.driver.find_element(*DEPARTURE_DROPDOWN)).select_by_visible_text(city)

    def select_destination(self, city):
        Select(self.driver.find_element(*DESTINATION_DROPDOWN)).select_by_visible_text(city)

    def click_find_flights(self):
        self.driver.find_element(*FIND_FLIGHTS_BUTTON).click()

    def choose_flight(self):
        self.driver.find_element(*CHOOSE_FLIGHT_BUTTON).click()

    def fill_passenger_details(self, name, address, city):
        self.driver.find_element(*INPUT_NAME).send_keys(name)
        self.driver.find_element(*INPUT_ADDRESS).send_keys(address)
        self.driver.find_element(*INPUT_CITY).send_keys(city)

    def click_purchase(self):
        self.driver.find_element(*PURCHASE_BUTTON).click()

    def go_to_destination_of_week(self):
        self.driver.find_element(*DEST_WEEK_LINK).click()

    def get_lufthansa_text(self):
        return self.driver.find_element(*LUFTHANSA_CELL).text

    def select_lufthansa(self):
        self.driver.find_element(*SELECT_AIRLINE_BUTTON).click()
