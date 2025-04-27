from ui.pages.pages_base import PageBase


class QAJobsPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_qa_jobs_btn(self):
        self.click(self.qa_jobs_locator)

    def click_department_container(self):
        self.click(locator=self.cookie_accept_locator)
        self.click(self.department_container)

    def select_quality_assurance(self):
        self.is_visible(locator=self.qa_category_locator, timeout=10)
        self.click(locator=self.qa_category_locator)

    def click_location_container(self):
        self.click(locator=self.location_container, timeout=10)

    def select_turkiye_ist(self):
        self.is_visible(locator=self.select_turkiye_ist_locator, timeout=10)
        self.click(locator=self.select_turkiye_ist_locator)

    def check_job_list(self):
        assert self.is_visible(locator=self.position_dep_locator, timeout=10)
        assert self.is_visible(locator=self.position_loc_locator, timeout=10)
        assert self.is_visible(locator=self.position_title_loc, timeout=10)

    def click_role_btn(self):
        self.click(locator=self.view_role_btn, timeout=10)

    def check_apply_btn(self):
        assert self.is_visible(locator=self.apply_job_button)

    def accept_privacy(self):
        self.click(locator=self.privacy_notice_accept, timeout=10)

    def qa_job_check(self):
        self.click_qa_jobs_btn()
        self.click_department_container()
        self.select_quality_assurance()
        self.click_location_container()
        self.select_turkiye_ist()
        self.scroll_window(x=0, y=700)
        self.check_job_list()
        self.click_role_btn()
        self.switch_to_window()
        self.accept_privacy()
        self.check_apply_btn()
