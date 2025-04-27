import os
from datetime import datetime
import pytest
from selenium import webdriver
from ui.pages.home_page import HomePage
from ui.pages.careers_page import CareersPage
from ui.pages.qa_jobs_page import QAJobsPage
from env_setup import HOMEPAGE_URL, QUALITY_ASSURANCE_URL, FULL_PATH
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def get_webdriver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))

    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver


@pytest.fixture()
def home_page(get_webdriver):
    get_webdriver.get(HOMEPAGE_URL)
    homepage = HomePage(get_webdriver)
    return homepage


@pytest.fixture()
def careers_page(get_webdriver):
    get_webdriver.get(HOMEPAGE_URL)
    careers_page = CareersPage(get_webdriver)
    return careers_page


@pytest.fixture()
def qa_jobs_page(get_webdriver):
    get_webdriver.get(QUALITY_ASSURANCE_URL)
    qa_jobs_page = QAJobsPage(get_webdriver)
    return qa_jobs_page


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failures(get_webdriver, request):
    failed_tests_count = request.session.testsfailed
    yield
    new_failed_tests_count = request.session.testsfailed
    if new_failed_tests_count > failed_tests_count:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_case_name = request.node.name
        screenshot = os.path.join(FULL_PATH, 'screens', f"screenshot_on_failures_{test_case_name}_{timestamp}.png")
        get_webdriver.get_screenshot_as_file(screenshot)
    get_webdriver.quit()
