import time
from pages.login_page import LoginPage

def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.open("https://spellmarket.ru/login")
    login_page.login("qwe@rt.y", "qwerty")
    time.sleep(5)
    expected_url = "https://spellmarket.ru/account"
    actual_url = login_page.get_current_url()
    assert actual_url == expected_url, f"Провалено"


def test_login_negative(driver):
    login_page = LoginPage(driver)
    login_page.open("https://spellmarket.ru/login")
    login_page.login("dashuyevin@mail.ru", "qweasz1234567890")
    time.sleep(5)
    expected_url = "https://spellmarket.ru/login"
    actual_url = login_page.get_current_url()
    assert actual_url == expected_url, f"Провалено"
    login_page.open("https://spellmarket.ru")
    login_page.open("https://spellmarket.ru/login")