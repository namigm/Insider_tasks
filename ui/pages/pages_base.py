from ui.base.selenium_base import BaseObject
from selenium.webdriver.common.by import By


class PageBase(BaseObject):
    insider_logo = (By.XPATH, "//img[@alt = 'insider_logo']")
    location_locator = (By.XPATH, "//h3[@class='category-title-media ml-0\' and contains("
                                  "text(), \'Our Locations')]")
    location_text_locator = (By.XPATH, '//p[@class="mt-5 mb-0 mt-lg-0 mx-auto pl-0" and contains(text(), "28 offices '
                                       'across 6 continents")]')
    teams_block_locator = (By.XPATH, "//div[@class='col-12 d-flex flex-wrap p-0 career-load-more']")
    life_block_locator = (By.CSS_SELECTOR, ".elementor-widget-wrap.elementor-element-populated.e-swiper-container")
    qa_jobs_locator = (By.XPATH, "//a[contains(@class, 'btn-outline-secondary') and text()='See all QA jobs']")
    location_container = (By.XPATH, "//span[@id ='select2-filter-by-location-container' and @class = "
                                    "'select2-selection__rendered']")
    cookie_accept_locator = (By.ID, "wt-cli-accept-all-btn")
    department_container = (By.ID, "select2-filter-by-department-container")
    qa_category_locator = (By.XPATH, "//span[@class = 'select2-selection__rendered' and @title='Quality Assurance']")
    select_turkiye_ist_locator = (By.XPATH, "//li[contains(text(), 'Istanbul, Turkiye')]")
    position_dep_locator = (By.XPATH, "//span[@class = 'position-department text-large font-weight-600 text-primary' "
                                      "and text() = 'Quality Assurance']")
    position_loc_locator = (By.XPATH, "//div[@class = 'position-location text-large' and text() = 'Istanbul, Turkiye']")
    position_title_loc = (By.XPATH, "//p[@class = 'position-title font-weight-bold' and contains(text(), 'Quality "
                                    "Assurance ')]")
    view_role_btn = (By.LINK_TEXT, "View Role")
    privacy_notice_accept = (By.XPATH, "(//button[@class = 'button button-sm cc-btn cc-dismiss' and text()= "
                                       "'Dismiss'])[1]")
    apply_job_button = (By.XPATH, "(//a[@class = 'postings-btn template-btn-submit shamrock' and text() = 'Apply for "
                                  "this job' ])[1]")
