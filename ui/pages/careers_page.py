from selenium.webdriver.common.by import By
from ui.base.selenium_base import BaseObject


class CareersPage(BaseObject):
    location_locator = (By.XPATH, "//h3[@class='category-title-media ml-0\' and contains("
                                  "text(), \'Our Locations')]")
    location_text_locator = (By.XPATH, '//p[@class="mt-5 mb-0 mt-lg-0 mx-auto pl-0" and contains(text(), "28 offices '
                                       'across 6 continents")]')
    teams_block_locator = (By.XPATH, "//div[@class='col-12 d-flex flex-wrap p-0 career-load-more']")
    life_block_locator = (By.CSS_SELECTOR, ".elementor-widget-wrap.elementor-element-populated.e-swiper-container")

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
