import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage

class FilterPage(BasePage):
    FILTER_BUTTON1 = (By.XPATH, '//*[@id="v-sin"]/input')
    FILTER_BUTTON2 = (By.XPATH, '//*[@id="v-100232164794230"]/input')
    FILTER_BUTTON3 = (By.XPATH, '//*[@id="v-100212079385988"]')

    def filter(self):
        time.sleep(3)
        self.driver.find_element(*self.FILTER_BUTTON1).click()
        time.sleep(5)
        self.driver.find_element(*self.FILTER_BUTTON2).click()
        time.sleep(5)
        self.driver.find_element(*self.FILTER_BUTTON3).click()

