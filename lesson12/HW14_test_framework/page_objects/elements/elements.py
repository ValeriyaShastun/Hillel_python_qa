from lesson12.HW14_test_framework.utilities.web_ui.action import Action
import lesson12.HW14_test_framework.page_objects.elements.elements_page_config as config


class Elements(Action):

    def __init__(self, driver):
        super().__init__(driver)

    def select_menu_item(self, item: str):
        if item in config.menu_items:
            dynamic_locator = [config.menu_item[0], config.menu_item[1].format(item)]
            self.click(tuple(dynamic_locator))
        else:
            self.logger.info(f"The menu item is incorrect, please select the right item from the list\n"
                             f"{config.menu_items}")

    ######################  CHECHBOX  #########################

    def expand_all(self):
        if self._wait.wait_until_element_located(config.tree_expanded, raise_exception=False):
            self.logger.info("Three element is already expanded")
        else:
            self.click(config.expand_all_button)
        return self

    def collapse_all(self):
        if not self._wait.wait_until_element_located(config.tree_expanded):
            self.logger.info("Three element is already collapsed")
        else:
            self.click(config.collapse_all_button)
        return self

    def locator_with_checkbox_name(self, locator, checkbox_name):
        list_to_process = checkbox_name.strip().replace(".doc", "").split()
        if len(list_to_process) > 1:
            checkbox_name_in_locator = list_to_process[0].lower() + list_to_process[1].capitalize()
            dynamic_locator = [locator[0], locator[1].format(checkbox_name_in_locator)]
        else:
            checkbox_name_in_locator = list_to_process[0].lower()
            dynamic_locator = [locator[0], locator[1].format(checkbox_name_in_locator)]
        selector = tuple(dynamic_locator)
        return selector

    def check_uncheck_checkbox_by_name(self, checkbox_name: str, check=True):
        """
        Checks or unchecks checkbox by name from UI
        :param checkbox_name: Name of checkbox from the UI
        :param check: check=True - will check checkbox in case it's not in the checked state already
                      check=False - will uncheck checkbox in case it's not in the unchecked state already
        :return: True - if checkbox is checked, False - if it's unchecked
        """
        return self.check_uncheck_checkbox(self.locator_with_checkbox_name(config.checkbox, checkbox_name),
                                           self.locator_with_checkbox_name(config.checkbox_state, checkbox_name),
                                           check=check)

    def checkbox_state_by_name(self, checkbox_name: str):
        """
        checks checkbox state by name from UI
        :param checkbox_name: Name of checkbox from the UI
        :return: True - if checkbox is checked, False - if it's unchecked
        """
        return self.checkbox_state(self.locator_with_checkbox_name(config.checkbox_state, checkbox_name))

    def check_uncheck_all_checkboxes(self, check=True):
        """
        checks that all checkboxes are checked/unchecked
        :param check: check=True - will check checkbox in case it's not in the checked state already
                      check=False - will uncheck checkbox in case it's not in the unchecked state already
        :return: True - if all checkboxes are checked, False - if all are unchecked, raise Exception if
        checkboxes are partially checked/unchecked
        """
        self.check_uncheck_checkbox(self.locator_with_checkbox_name(
            config.checkbox, config.all_checkbox_names[0]),
            self.locator_with_checkbox_name(
                config.checkbox_state, config.all_checkbox_names[0]),
            check=check)
        checkboxes = self._wait.wait_until_elements_located(config.checkboxes_state)
        list_to_check = []
        for _ in checkboxes:
            if self.checkbox_state(config.checkboxes_state):
                list_to_check.append(True)
            else:
                list_to_check.append(False)
        if check:
            if all(set(list_to_check)) and list_to_check != []:
                return True
            elif False in set(list_to_check):
                raise Exception("Some checkboxes are checked and some are not after checking all checkboxes")
        else:
            if len(set(list_to_check)) == 1 and False in set(list_to_check):
                return False
            else:
                raise Exception("Some checkboxes are checked and some are not after unchecking all checkboxes")

    def get_you_have_selected_checkboxes(self):
        """
        Getting selected checkboxes in statement "You have selected : <checkbox_name>, <checkbox_name>"
        :return: list of selected checkboxes
        """
        checkboxes_selected = self._wait.wait_until_elements_located(config.you_have_selected_checkboxes_name)
        return [self.get_text(checkbox) for checkbox in checkboxes_selected]

    def checkboxes_name_for_you_have_selected_checkboxes(self, checkboxes_names):
        """
        Returning checkbox name as it should be reflected in statement
        "You have selected : <checkbox_name>, <checkbox_name>"
        :param checkboxes_names: list of names of checkbox from the UI
        :return: list of checkbox names for field "You have selected : <checkbox_name>, <checkbox_name>"
        """
        list_checkboxes_names = []
        for name in checkboxes_names:
            name_in_list = name.strip().replace(".doc", "").split()
            checkbox_name_in_you_have_selected = name_in_list[0].lower() + name_in_list[1].capitalize() \
                if len(name_in_list) > 1 else name_in_list[0].lower()
            list_checkboxes_names.append(checkbox_name_in_you_have_selected)
        return list_checkboxes_names

    def verify_tree_expanded_collapsed(self):
        """
        Verifying whether checkbox tree is expanded or collapsed
        :return: False for collapsed, True for expanded
        """
        try:
            self._wait.wait_until_element_located(config.tree_expanded)
            return True
        except:
            return False
