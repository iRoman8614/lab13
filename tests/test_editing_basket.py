from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.basket_editing_page import BasketEditionPage

def test_basket_editing_positive(driver):
    basket_editing_page = BasketEditionPage(driver)
    basket_editing_page.action1()
    driver.execute_script("window.scrollTo(0, 0)")
    basket_editing_page.action2()
    driver.execute_script("window.scrollTo(0, 0)")
    basket_editing_page.action3()
    driver.execute_script("window.scrollTo(0, 0)")
    basket_editing_page.action4()
    driver.execute_script("window.scrollTo(0, 0)")
    basket_editing_page.action4()
    driver.execute_script("window.scrollTo(0, 0)")
    basket_editing_page.action4()
    driver.execute_script("window.scrollTo(0, 0)")
    answer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"simplecheckout_form_0\"]/div/div[1]"))
    )
    assert "Ваша корзина пуста!" == answer.text, f"Failed + " + answer.text