import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager




logger = logging.getLogger()
logger.setLevel('INFO')



@pytest.fixture()
def get_driver():
    logger.info(msg='\nFixture "get_driver" start')
    def driver_factory(driver_name: str):
        """
        Returns driver instance corresponding to passed parameter.
        :param driver_name: driver name, possible options: "firefox", "chrome", "edge"
        :return: driver instance
        """
        driver = None
        options = ["firefox", "chrome", "edge"]
        if driver_name == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif driver_name == "firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        elif driver_name == "edge":
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        elif driver_name not in options:
            logger.info("The driver parameter is incorrect, should be one of {0}, {1}, {2}".format(*options))
        return driver

    yield driver_factory
    # driver.quit() # FIXME
    logger.info(msg='\nFixture "get_driver" finished')

