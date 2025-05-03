from ui.base.selenium_base import BaseObject
from selenium.webdriver.common.by import By


class HomePage(BaseObject):
    insider_logo = (By.XPATH, "//img[@alt = 'insider_logo']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_opened(self):
        assert self.is_visible(self.insider_logo)
