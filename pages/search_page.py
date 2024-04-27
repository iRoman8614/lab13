import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    SRC_BUTTON = (By.XPATH, '//*[@class="sign search-page-invisible"]')
    SRC_INPUT = (By.XPATH, '//*[@id="search"]/input')

    def search(self, tovar):
        self.driver.find_element(*self.SRC_INPUT).click()
        self.driver.find_element(*self.SRC_INPUT).send_keys(tovar)
        self.driver.find_element(*self.SRC_INPUT).send_keys(Keys.ENTER)
