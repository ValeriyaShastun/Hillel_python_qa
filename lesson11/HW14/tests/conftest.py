import logging
import pytest

from selenium.webdriver import Chrome, Edge, Firefox

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.fixture()
def chrome_driver():
    logger.info(msg='\nFixture "chrome_driver" start')
    driver_chrome = Chrome("/usr/local/bin/chromedriver")
    yield driver_chrome
    driver_chrome.quit()
    logger.info(msg='\nFixture "chrome_driver" finished')


@pytest.fixture()
def firefox_driver():
    logger.info(msg='\nFixture "firefox_driver" start')
    driver_firefox = Firefox("/usr/local/bin/")  # geckodriver
    yield driver_firefox
    driver_firefox.quit()
    logger.info(msg='\nFixture "firefox_driver" finished')


@pytest.fixture()
def edge_driver():
    logger.info(msg='\nFixture "edge_driver" start')
    driver_edge = Edge("/usr/local/bin/msedgedriver")
    yield driver_edge
    driver_edge.quit()
    logger.info(msg='\nFixture "edge_driver" finished')
