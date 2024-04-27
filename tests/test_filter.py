import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.filter_page import FilterPage

def test_filter_positive(driver):
    filter_page = FilterPage(driver)
    filter_page.filter()
    time.sleep(8)
    answer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[4]/div[2]'))
    )
    assert "Показано с 1 по 1 из 1 (всего 1 страниц)" == answer.text, f"Failed + " + answer.text