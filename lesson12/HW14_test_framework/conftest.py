import datetime
from lesson12.HW14_test_framework.CONSTS import ROOT_DIR
from lesson12.HW14_test_framework.page_objects.home_page.home_page import HomePage
from lesson12.HW14_test_framework.utilities.driver_factory import DriverFactory
from lesson12.HW14_test_framework.utilities.read_run_settings import ReadConfig
from lesson12.HW14_test_framework.utilities.logger import Logger as logger
import pytest
import os

logger = logger.getLogger()


@pytest.fixture(scope="module")
def start_driver():
    logger.info("Start of fixture create_driver")
    driver = DriverFactory.create_driver(driver_id=int(ReadConfig.get_driver_id()), is_headless=False)
    driver.get(ReadConfig.get_application_url())
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("End of fixture create_driver")


@pytest.fixture(scope="module", autouse=True)
def clear_screenshot_folder_before_run():
    filelist = [file for file in os.listdir(f"{ROOT_DIR}/tests/screenshots") if file.endswith(".jpg")]
    for file in filelist:
        os.remove(os.path.join(f"{ROOT_DIR}/tests/screenshots", file))
    yield


@pytest.fixture(autouse=True)
def failure_tracking_fixture(request, start_driver):
    tests_failed_initially = request.session.testsfailed
    yield
    tests_failed_finally = request.session.testsfailed
    if tests_failed_finally - tests_failed_initially == 1:
        start_driver.save_screenshot(f"{ROOT_DIR}/tests/screenshots/{request.node.nodeid}_"
                                     f"{datetime.datetime.now().strftime('%Y-%m-%d - %H:%M')}.jpg")
        logger.info(f"a test {request.node.nodeid} has failed!")


@pytest.fixture()
def home_page_get(start_driver):
    return HomePage(start_driver)


@pytest.fixture()
def get_elements_item(home_page_get):
    def wrapper(bar_menu_item):
        home_page = home_page_get
        home_page.logger.info("user is on the home page")
        elements = home_page.elements
        elements.select_menu_item(bar_menu_item)
        return elements

    yield wrapper
