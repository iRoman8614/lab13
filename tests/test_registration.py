import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage

def test_registration_positive(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open("https://spellmarket.ru/simpleregister")
    rand = round(random.uniform(1, 10000))
    emai = "dashuyevin" + str(rand) + "@mail.ru"
    number = "+78005553535" + str(rand)
    name = "Ivan" + str(rand)
    registration_page.register(emai, "qweasz123", name, number)
    #answer = WebDriverWait(driver, 10).until(
    #    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1'))
    #)
    #assert "Ваша учетная запись создана!" == answer.text, f"Failed + " + answer.text
    time.sleep(5)
    expected_url = 'https://spellmarket.ru/index.php?route=account/success'
    actual_url = registration_page.get_current_url()
    assert actual_url == expected_url, f"Провалено"