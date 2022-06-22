import lesson12.HW14_test_framework.page_objects.home_page.home_page_config as config
from lesson12.HW14_test_framework.page_objects.elements.elements import Elements
from lesson12.HW14_test_framework.utilities.web_ui.action import Action


class HomePage(Action):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def elements(self):
        self.click(config.elements_card)
        return Elements(self._driver)

    # def click_forms(self): # TODO the rest of classes
    #     self.click(config.forms_card)
    #     return Forms(self._driver)
