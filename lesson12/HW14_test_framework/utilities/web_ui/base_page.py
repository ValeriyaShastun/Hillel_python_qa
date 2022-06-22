from lesson12.HW14_test_framework.utilities.logger import Logger as logger


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.logger = logger.getLogger()

    def click(self, locator):
        element = self._wait.wait_until_element_clickable(locator)
        if element is not None:
            self._driver.execute_script("arguments[0].scrollIntoView()", element)
            element.click()

    def get_text(self, element):
        if element is not None:
            return element.text

    def send_keys(self, locator, value, is_clear=False):
        element = self._wait.wait_until_element_located(locator)
        if element is not None:
            self._driver.execute_script("arguments[0].scrollIntoView()", element)
            if is_clear:
                element.clear()
            element.send_keys(value)

    def get_attribute(self, locator, attribute_name):
        element = self._wait.wait_until_element_located(locator)
        if element is not None:
            return element.get_attribute(attribute_name)

    def check_page_title(self, page_title):
        if self.title == page_title:
            self.logger.info(f"Page title is correspondent to {page_title}")
            return True
        else:
            self.logger.info(f"Page title is not correspondent to {page_title}")
            return False

    @property
    def title(self):
        return self._driver.title
