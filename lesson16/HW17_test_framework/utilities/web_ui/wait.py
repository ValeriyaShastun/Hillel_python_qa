from lesson12.HW14_test_framework.utilities.web_ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Wait(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _wait(self, timeout=10):
        return WebDriverWait(self._driver, timeout)

    def wait_until_element_located(self, locator, timeout=10, raise_exception=True):
        """
        Waits until element is reflected on the page and returns element found
        :param locator: locator of the element to be found
        :param timeout: timeout within which element will be searched
        :return: webelement if it is present on the page, None if element is not found
        """
        web_element = None
        try:
            web_element = self._wait(timeout=timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            if raise_exception:
                raise Exception(e)
            else:
                self.logger.info(f"The element is not found in the page\n EXCEPTION: {e}")
        return web_element

    def wait_until_elements_located(self, locator, timeout=10, raise_exception=True):
        """
        Waits until element is reflected on the page and returns element found
        :param locator: locator of the element to be found
        :param timeout: timeout within which element will be searched
        :return: webelement if it is present on the page, None if element is not found
        """
        web_element = None
        try:
            web_element = self._wait(timeout=timeout).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            if raise_exception:
                raise Exception(e)
            else:
                self.logger.info(f"The elements are not found in the page\n EXCEPTION: {e}")
        return web_element

    def wait_until_element_clickable(self, locator, timeout=10):
        """
        Waits until element is reflected on the page and returns element found
        :param locator: locator of the element to be found
        :param timeout: timeout within which element will be searched
        :return: webelement if it is present on the page, None if element is not found
        """
        web_element = None
        try:
            web_element = self._wait(timeout=timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            self.logger.info(f"The element is not clickable\n EXCEPTION: {e}")
        return web_element
