import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
class RegistrationPage(BasePage):
    EMAIL_INPUT = (By.XPATH,'//*[@id="register_email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="register_password"]')
    PASSWORD2_INPUT = (By.XPATH, '//*[@id="register_confirm_password"]')
    NAME_INPUT = (By.XPATH, '//*[@id="register_firstname"]')
    MOBILE_INPUT = (By.XPATH,'//*[@id="register_telephone"]')
    ENTER_BUTTON = (By.XPATH,'//*[@id="simpleregister_button_confirm"]/span')

    def register(self, email, password, name, mobile):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.PASSWORD2_INPUT).send_keys(password)
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.MOBILE_INPUT).send_keys(mobile)
        time.sleep(5)
        self.driver.find_element(*self.ENTER_BUTTON).click()
        time.sleep(5)

