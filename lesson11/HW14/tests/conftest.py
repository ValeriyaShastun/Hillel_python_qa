import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, Edge, Firefox

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.fixture()
def generate_data_for_test() -> dict:
    logger.info(msg='\nFixture "generate_data_for_test" start')
    dict_login_data = {"username": "valeriia_is_here",
                       "password": "valeriiatest",
                       "login_url": "http://www.testyou.in/Login.aspx?ReturnUrl=%2fStudent%2fStudentIndex.aspx",
                       "home_page_url": "http://www.testyou.in/Student/StudentIndex.aspx",
                       "username_selector": '[name$="Container$txtUserLogin"]',
                       "password_selector": '[name$="Container$txtPassword"]',
                       "login_button_selector": '[type="submit"][name$="btnLoginn"]'}
    yield dict_login_data
    logger.info(msg='\nFixture "generate_data_for_test" finished')


@pytest.fixture()
def login():
    logger.info(msg='\nFixture "login" start')

    def wrapper(driver, data_for_test):
        driver.find_element(By.CSS_SELECTOR, data_for_test["username_selector"]).send_keys(data_for_test["username"])
        driver.find_element(By.CSS_SELECTOR, data_for_test["password_selector"]).send_keys(data_for_test["password"])
        driver.find_element(By.CSS_SELECTOR, data_for_test["login_button_selector"]).click()

    yield wrapper
    logger.info(msg='\nFixture "login" finished')


@pytest.fixture()
def chrome_driver() -> Chrome:
    logger.info(msg='\nFixture "chrome_driver" start')
    driver_chrome = Chrome("/usr/local/bin/chromedriver")
    yield driver_chrome
    driver_chrome.quit()
    logger.info(msg='\nFixture "chrome_driver" finished')


@pytest.fixture()
def firefox_driver() -> Firefox:
    logger.info(msg='\nFixture "firefox_driver" start')
    driver_firefox = Firefox("/usr/local/bin/")  # geckodriver
    yield driver_firefox
    driver_firefox.quit()
    logger.info(msg='\nFixture "firefox_driver" finished')


@pytest.fixture()
def edge_driver() -> Edge:
    logger.info(msg='\nFixture "edge_driver" start')
    driver_edge = Edge("/usr/local/bin/msedgedriver")
    yield driver_edge
    driver_edge.quit()
    logger.info(msg='\nFixture "edge_driver" finished')
