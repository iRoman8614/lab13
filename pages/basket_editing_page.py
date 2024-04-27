import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from .base_page import BasePage

class BasketEditionPage(BasePage):
    PLUS_BUTTON1 = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr[1]/td[4]/div/span[2]/button[1]')
    PLUS_BUTTON2 = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr[2]/td[4]/div/span[2]/button[1]')
    MINUS_BUTTON = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr[2]/td[4]/div/span[1]/button')
    DELETE_BUTTON = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr[1]/td[4]/div/span[2]/button[2]')

    def action1(self):
        self.driver.find_element(*self.PLUS_BUTTON1).click()
        time.sleep(5)

    def action2(self):
        self.driver.find_element(*self.PLUS_BUTTON2).click()
        time.sleep(5)

    def action3(self):
        self.driver.find_element(*self.MINUS_BUTTON).click()
        time.sleep(5)

    def action4(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()
        time.sleep(5)