from selenium.webdriver.common.by import By
from ui.pages.pages_base import PageBase


class CareersPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    def select_company(self):
        company_link = self.driver.find_element(By.LINK_TEXT, "Company")
        self.click(locator=company_link, timeout=5)

    def click_career(self):
        career_link = self.driver.find_element(By.LINK_TEXT, "Careers")
        self.click(locator=career_link, timeout=5)

    def check_blocks(self):
        assert self.is_visible(locator=self.location_locator)
        assert self.is_visible(locator=self.location_text_locator)
        assert self.is_visible(locator=self.teams_block_locator)
        assert self.is_visible(locator=self.life_block_locator)

    def select_careers(self):
        self.select_company()
        self.click_career()
        self.check_blocks()
