from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.test_login import test_login_positive
from tests.test_login import test_login_negative
from tests.test_registration import test_registration_positive
from tests.test_basket import test_busket_positive
from tests.test_editing_basket import test_basket_editing_positive
from tests.test_navigation import quit
from tests.test_navigation import home
from tests.test_navigation import foils
from tests.test_search import test_search_positive
from tests.test_filter import test_filter_positive


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def teardown_driver(driver):
    driver.quit()


if __name__ == "__main__":
    driver = setup_driver()

    try:
        test_registration_positive(driver)
        print("Test registration_positive passed")
    except AssertionError as e:
        print(f"Test registration_positive failed: {e}")

    try:
        quit(driver)
        print("test_navigation quit passed")
    except AssertionError as e:
        print(f"Test quit failed: {e}")

    try:
        home(driver)
        print("test_navigation go home passed")
    except AssertionError as e:
        print(f"Test quit failed: {e}")

    try:
        test_login_negative(driver)
        print("негативный тест провалился")
    except AssertionError as e:
        print(f"Test login_negative failed: {e}")

    try:
        home(driver)
        print("test_navigation go home passed")
    except AssertionError as e:
        print(f"Test quit failed: {e}")

    try:
        test_login_positive(driver)
        print("Test login_positive passed")
    except AssertionError as e:
        print(f"Test login_positive failed: {e}")

    try:
        test_search_positive(driver)
        print("Test search_positive passed")
    except AssertionError as e:
        print(f"Test search_positive failed: {e}")

    try:
        test_busket_positive(driver)
        print("Test busket_positive passed")
    except AssertionError as e:
        print(f"Test busket_positive failed: {e}")

    try:
        test_basket_editing_positive(driver)
        print("Test basket_editing_positive passed")
    except AssertionError as e:
        print(f"Test basket_editing_positive failed: {e}")

    try:
        foils(driver)
        print("test_navigation go to foils passed")
    except AssertionError as e:
        print(f"Test quit failed: {e}")

    try:
        test_filter_positive(driver)
        print("Test filter_positive passed")
    except AssertionError as e:
        print(f"Test filter_positive failed: {e}")

    teardown_driver(driver)