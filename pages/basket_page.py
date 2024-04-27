import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class BasketPage(BasePage):
    ADD_CONTENT1 = (By.XPATH, '//*[@id="content"]/div[4]/div[6]/div/div[2]/div[2]/div[1]/a')
    ADD_CONTENT2 = (By.XPATH, '//*[@id="content"]/div[4]/div/div/div[2]/div[2]/div[1]/a')
    ADD_CONTENT3 = (By.XPATH, '//*[@id="content"]/div[4]/div[8]/div/div[2]/div[2]/div[1]/a')
    BASKET_BUTTON = (By.XPATH, '//*[@id="cart-total"]')
    BASKET_BUTTON2 = (By.XPATH, '//*[@id="cart"]/div/ul/li[2]/div/p/a[1]')

    def basket(self):
        time.sleep(1)
        self.driver.find_element(*self.ADD_CONTENT1).click()
        time.sleep(1)
        self.driver.find_element(*self.ADD_CONTENT2).click()
        time.sleep(1)
        self.driver.find_element(*self.ADD_CONTENT3).click()
        time.sleep(5)

    def next(self):
        self.driver.execute_script("window.scrollBy(0,0)", "")
        self.driver.find_element(*self.BASKET_BUTTON).click()
        time.sleep(5)
