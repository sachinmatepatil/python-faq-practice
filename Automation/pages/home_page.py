from  selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage

class HomePage(BasePage):
    def get_links(self):
        return self.get_elements(By.TAG_NAME, "a")
