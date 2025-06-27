from selenium.webdriver.support.select import Select
from Pages.FlightBookingPage import FlightBookingPage
from Utilities.ReadProperties import ReadConfig
from Testcases.conftest import save_ss
import pytest


def test_FB1(driver):
    driver.get(ReadConfig.get_base_url())
    booking_page = FlightBookingPage(driver)
    booking_page.select_departure("Boston")
    booking_page.select_destination("London")
    booking_page.click_find_flights()


def test_FB2(driver):
    assert "Flights from Boston to London" in driver.page_source


def test_FB3(driver):
    booking_page = FlightBookingPage(driver)
    booking_page.choose_flight()
    assert "BlazeDemo - reserve" in driver.title


def test_FB4(driver):
    booking_page = FlightBookingPage(driver)
    booking_page.fill_passenger_details(ReadConfig.get_username(), "INDIA", "ABC")
    booking_page.click_purchase()


def test_FB5(driver):
    save_ss(driver, "ticket.png")


def test_FB6(driver):
    booking_page = FlightBookingPage(driver)
    booking_page.go_to_destination_of_week()
    assert "Destination of the week: Hawaii !" in driver.page_source
    save_ss(driver, "DOW.png")


def test_FB7(driver):
    booking_page = FlightBookingPage(driver)
    Select(driver.find_element_by_xpath("/html[1]/body[1]/div[3]/form[1]/select[1]")).select_by_index(4)
    Select(driver.find_element_by_xpath("/html[1]/body[1]/div[3]/form[1]/select[2]")).select_by_index(5)
    booking_page.click_find_flights()
    airlines = booking_page.get_lufthansa_text()
    booking_page.select_lufthansa()
    assert airlines in driver.page_source


@pytest.mark.parametrize(
    "departure,destination,name,address,city",
    [
        (dep, arr, pname, paddr, pcity)
        for dep in ReadConfig.get_departure_cities()
        for arr in ReadConfig.get_arrival_cities()
        for pname in ReadConfig.get_passenger_names()
        for paddr in ReadConfig.get_passenger_addresses()
        for pcity in ReadConfig.get_passenger_cities()
    ][:50]  # Limit to 50 combinations for demonstration
)
def test_bulk_flight_booking_cases(driver, departure, destination, name, address, city):
    driver.get(ReadConfig.get_base_url())
    booking_page = FlightBookingPage(driver)
    booking_page.select_departure(departure)
    booking_page.select_destination(destination)
    booking_page.click_find_flights()
    booking_page.choose_flight()
    booking_page.fill_passenger_details(name, address, city)
    booking_page.click_purchase()
    # Optionally, assert booking confirmation


