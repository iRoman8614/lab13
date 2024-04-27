from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage

def test_search_positive(driver):
    search_page = SearchPage(driver)
    tovar = "teferi"
    search_page.search(tovar)
    answer = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/h2[2]"))
    )
    assert answer.text == "Результаты поиска", f"Failed"