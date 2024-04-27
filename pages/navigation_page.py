import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
class NavigationPage(BasePage):
    QUIT_BUTTON = (By.XPATH, '//*[@id="header"]/div[1]/div[3]/div/ul/li[2]/a/span')
    MAIN_BUTTON = (By.XPATH, '//*[@id="logo"]/a/img')
    FOIL_BUTTON = (By.XPATH, '//*[@id="main-menu-item-6"]/a/span')

    def navigation(self):
        self.driver.find_element(*self.MAIN_BUTTON).click()
        time.sleep(5)

    def qiut(self):
        self.driver.find_element(*self.QUIT_BUTTON).click()
        time.sleep(5)

    def foils(self):
        self.driver.find_element(*self.FOIL_BUTTON).click()
        time.sleep(5)