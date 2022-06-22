from lesson12.HW14_test_framework.utilities.web_ui.base_page import BasePage
from lesson12.HW14_test_framework.utilities.web_ui.wait import Wait


class Action(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = Wait(driver)

    ######################  CHECHBOX  #########################

    def checkbox_state(self, locator_for_state_check):
        """
        checks checkbox state
        :return: True if checked, False if unchecked
        """
        if "uncheck" in self.get_attribute(locator_for_state_check, "class") or "half-check" in self.get_attribute(
                locator_for_state_check, "class"):
            return False
        else:
            return True

    def check_uncheck_checkbox(self, locator, locator_for_state_check, check=True):
        """
        Check or uncheck checkbox
        :param locator: locator of the element
        :param check: check=True - will check checkbox in case it's not in the checked state already
                      check=False - will uncheck checkbox in case it's not in the unchecked state already
        :return: True - if checkbox is checked, False - if it's unchecked
        """
        checkbox = self._wait.wait_until_element_clickable(locator)
        if check:
            if not self.checkbox_state(locator_for_state_check):
                self._driver.execute_script("arguments[0].scrollIntoView()", checkbox)
                checkbox.click()
                return True
            else:
                self.logger.info("The Checkbox is already checked")
                return True
        else:
            if self.checkbox_state(locator_for_state_check):
                self._driver.execute_script("arguments[0].scrollIntoView()", checkbox)
                checkbox.click()
                return False
            else:
                self.logger.info("The Checkbox is already unchecked")
                return False
