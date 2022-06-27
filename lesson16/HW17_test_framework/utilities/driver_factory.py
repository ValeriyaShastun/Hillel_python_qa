from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as ServiceEdge
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    CHROME = 1
    CHROMIUM = 2
    FIREFOX = 3
    EDGE = 4

    @staticmethod
    def create_driver(driver_id, is_headless):
        if DriverFactory.CHROME == driver_id:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=chrome_options)
        elif DriverFactory.CHROMIUM == driver_id:
            driver = webdriver.Chrome(
                service=ServiceChrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        elif DriverFactory.FIREFOX == driver_id:
            driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()))
        elif DriverFactory.EDGE == driver_id:
            driver = webdriver.Edge(service=ServiceEdge(EdgeChromiumDriverManager().install()))
        else:
            driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()))

        return driver
