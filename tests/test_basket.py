import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.basket_page import BasketPage

def test_busket_positive(driver):
    basket_page = BasketPage(driver)
    basket_page.basket()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0)")
    basket_page.next()
    time.sleep(10)
    expected_url = "https://spellmarket.ru/simplecheckout"
    actual_url = basket_page.get_current_url()
    assert actual_url == expected_url, f"Тест не пройден: ожидался URL '{expected_url}', но был получен '{actual_url}'"