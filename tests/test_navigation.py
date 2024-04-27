import time
from pages.navigation_page import NavigationPage

def quit(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.qiut()
    time.sleep(5)

def home(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.navigation()
    time.sleep(5)

def foils(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.foils()
    time.sleep(5)