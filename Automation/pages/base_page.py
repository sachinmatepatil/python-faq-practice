# pages/base_page.py

from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_elements(self, by, value):
        return self.driver.find_elements(by, value)