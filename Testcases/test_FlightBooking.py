from selenium.webdriver.support.select import Select
from Pages.FlightBookingPage import FlightBookingPage
from Utilities.ReadProperties import ReadConfig
from Testcases.conftest import save_ss


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


