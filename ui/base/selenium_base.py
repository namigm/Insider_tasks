from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.custom_exception import VisibleElementNotFound, ClickableElementNotFound
from support.logger import save_log


class BaseObject:
    LOG = save_log()

    def __init__(self, driver):
        self.driver = driver

    def _wait_element(self, timeout=5):
        return WebDriverWait(self.driver, timeout)

    def _is_clickable(self, locator, timeout=5):
        try:
            clickable_element = self._wait_element(timeout).until(ec.element_to_be_clickable(locator))
            self.LOG.info(f"Requested element - {locator} is clickable")
            return clickable_element

        except TimeoutException:
            self.LOG.error(f"Requested element - {locator} isn't clickable within {timeout} seconds")
            raise ClickableElementNotFound("Element is not clickable")

    def is_visible(self, locator, timeout=5):

        try:
            visible_element = self._wait_element(timeout).until(ec.visibility_of_element_located(locator))
            self.LOG.info(f"Requested element - {locator} is visible")
            return visible_element

        except TimeoutException:
            self.LOG.error(f"Requested element - {locator} isn't visible within {timeout} seconds")
            raise VisibleElementNotFound("Element is not visible")

    def click(self, locator, timeout=5):
        self._is_clickable(locator, timeout).click()
        self.LOG.info(f"Requested element - {locator} is clicked")

    def scroll_window(self, x=0, y=0):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def switch_to_window(self):
        all_windows = self.driver.window_handles
        current_window = self.driver.current_window_handle
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
