from ui.pages.pages_base import PageBase


class HomePage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    def is_opened(self):
        assert self.is_visible(self.insider_logo)
