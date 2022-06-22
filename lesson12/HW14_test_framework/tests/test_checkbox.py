import pytest
import lesson12.HW14_test_framework.page_objects.elements.elements_page_config as config

bar_menu_check_box = "Check Box"


@pytest.mark.parametrize("checkbox_name", ["Desktop", "Public", "Word File.doc"])
def test_check_several_checkboxes_by_name(home_page_get, checkbox_name, get_elements_item):
    """
     Description: test clicks corresponding checkboxes and checks that their state after it is True

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check checkboxes with corresponding names
     2. Receive state of the checkboxes with corresponding name
     3. Check that checkboxes state is eq to True (i.e. it's checked)

     Expected:
     1. After checking exact checkboxes their state is eq to True (i.e. it's checked)
     """
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_checkbox_by_name(checkbox_name, check=True)
    checkbox_state = elements.checkbox_state_by_name(checkbox_name)
    assert checkbox_state == True, f"Checkbox should be checked, with state True, but it is with state {checkbox_state}"


def test_check_one_checkbox_by_name(home_page_get, get_elements_item):
    """
     Description: test clicks corresponding checkboxes and checks that their state after it is True

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check checkbox with corresponding name
     2. Receive state of the checkbox with corresponding name
     3. Check that checkbox state is eq to True (i.e. it's checked)

     Expected:
     1. After checking exact checkbox it's state is eq to True (i.e. it's checked)
     """
    checkbox_name = "Public"
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_checkbox_by_name(checkbox_name, check=True)
    checkbox_state = elements.checkbox_state_by_name(checkbox_name)
    assert checkbox_state == True, f"Checkbox should be checked, with state True, but it is with state {checkbox_state}"


def test_collapse_all_after_checkbox_check(home_page_get, get_elements_item):
    """
     Description: test clicks corresponding checkbox, collapses entire tree, expands entire tree
     checks their state after it

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check checkbox with corresponding name
     2. Receive state of the checkbox with corresponding name
     3. Press "Collapse All" button [-] and press "Expand All" button [+]
     4. Check that checkbox state is eq to True (i.e. it's checked)

     Expected:
     1. After checking exact checkbox, collapsing and expanding tree again checkbox's state is
     eq to True (i.e. it's checked)
     """
    checkbox_name = "Veu"
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_checkbox_by_name(checkbox_name, check=True)
    elements.collapse_all()
    elements.expand_all()
    checkbox_state = elements.checkbox_state_by_name(checkbox_name)
    assert checkbox_state == True, f"Checkbox {checkbox_name} should be checked, with state True, " \
                                   f"but it is with state {checkbox_state}"


def test_uncheck_checkbox_by_name(home_page_get, get_elements_item):
    """
     Description: test checks and then unchecks corresponding checkbox and
     verifies that its state after operation is False

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check checkbox with corresponding name
     2. Uncheck checkbox with corresponding name
     3. Receive state of the checkbox with corresponding name
     4. Check that checkbox state is eq to False (i.e. it's NOT checked)

     Expected:
     1. After unchecking exact checkbox it's state is eq to False (i.e. it's NOT checked)
     """
    checkbox_name = "React"
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_checkbox_by_name(checkbox_name, check=True)
    elements.check_uncheck_checkbox_by_name(checkbox_name, check=False)
    checkbox_state = elements.checkbox_state_by_name(checkbox_name)
    assert checkbox_state == False, f"Checkbox should NOT be checked, with state False, " \
                                    f"but it is with state {checkbox_state}"


def test_check_all_checkboxes(home_page_get, get_elements_item):
    """
     Description: test checks all checkboxes and
     verifies that state of all checkboxes after operation is True

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check all checkboxes
     2. Receive state of all checkboxes with corresponding name

     Expected:
     1. After checking all checkboxes their state is eq to True (i.e. they are checked)
     """
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_all_checkboxes(check=True)
    for checkbox in config.all_checkbox_names:
        checkbox_state = elements.checkbox_state_by_name(checkbox)
        assert checkbox_state == True, f"Checkbox should be checked, with state True, " \
                                       f"but it is with state {checkbox_state}"


def test_uncheck_all_checkboxes(home_page_get, get_elements_item):
    """
     Description: test unchecks all checkboxes and
     verifies that state of all checkboxes after operation is True

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Uncheck all checkboxes
     2. Receive state of all checkboxes with corresponding name

     Expected:
     1. After unchecking all checkboxes their state is eq to False (i.e. they are NOT checked)
     """
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_all_checkboxes(check=False)
    for checkbox in config.all_checkbox_names:
        checkbox_state = elements.checkbox_state_by_name(checkbox)
        assert checkbox_state == False, f"Checkbox should NOT be checked, with state False, " \
                                        f"but it is with state {checkbox_state}"


def test_name_of_one_selected_checkbox(home_page_get, get_elements_item):
    """
     Description: test checks that checked checkbox name is in block
     "You have selected : <checkbox_name>, <checkbox_name>"

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check checkbox with corresponding name
     2. Get checkbox name from the block "You have selected : <checkbox_name>, <checkbox_name>"
     3. Check that name in the block corresponds to the name of checkbox checked

     Expected:
     1. After checking exact checkbox it's name appears in block
     "You have selected : <checkbox_name>, <checkbox_name>"
     """
    checkbox_name = "React"
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_checkbox_by_name(checkbox_name, check=True)
    selected_checkboxes = elements.get_you_have_selected_checkboxes()
    name_for_comparison = elements.checkboxes_name_for_you_have_selected_checkboxes([checkbox_name])
    assert selected_checkboxes == name_for_comparison, f'Checkbox name selected -> {selected_checkboxes} does " \
                                                             f"not correspond to the name in "You have selected : ' \
                                                       f'<checkbox_name>, <checkbox_name>" block ' \
                                                       f'-> {name_for_comparison}'


def test_name_of_unselected_checkbox(home_page_get, get_elements_item):
    """
     Description: test checks that unchecked checkbox name is not in block
     "You have selected : <checkbox_name>, <checkbox_name>"

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]
     5. Unselect all checkboxes

     Steps:
     1. Check two checkboxes with corresponding names
     2. Uncheck one of the checkboxes
     3. Get checkbox names from the block "You have selected : <checkbox_name>, <checkbox_name>"
     3. Check that name in the block corresponds to the name of checkbox checked and there is no unselected
     checkbox name

     Expected:
     1. After unchecking exact checkbox it's name disappears from block
     "You have selected : <checkbox_name>, <checkbox_name>"
     """
    checkboxes_names = ["General", "Excel File.doc"]
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_all_checkboxes(check=True)
    elements.check_uncheck_all_checkboxes(check=False)
    for checkbox in checkboxes_names:
        elements.check_uncheck_checkbox_by_name(checkbox, check=True)
    elements.check_uncheck_checkbox_by_name(checkboxes_names[1], check=False)
    selected_checkboxes = elements.get_you_have_selected_checkboxes()
    name_for_comparison = elements.checkboxes_name_for_you_have_selected_checkboxes([checkboxes_names[0]])
    assert selected_checkboxes == name_for_comparison, f'Checkbox name selected -> {selected_checkboxes} does " \
                                                             f"not correspond to the name in "You have selected : ' \
                                                       f'<checkbox_name>, <checkbox_name>" block ' \
                                                       f'-> {name_for_comparison}'


def test_names_of_several_selected_checkboxes(home_page_get, get_elements_item):
    """
     Description: test checks that checked checkboxes names are in block
     "You have selected : <checkbox_name>, <checkbox_name>"

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Check checkboxes with corresponding names
     2. Get checkbox names from the block "You have selected : <checkbox_name>, <checkbox_name>"
     3. Check that names in the block correspond to the names of checkboxes checked

     Expected:
     1. After checking exact checkboxes their name appear in block
     "You have selected : <checkbox_name>, <checkbox_name>", no other checkboxes are in the list
     """
    checkboxes_names = ["Notes", "React", "Angular"]
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.check_uncheck_all_checkboxes(check=True)
    elements.check_uncheck_all_checkboxes(check=False)
    for checkbox in checkboxes_names:
        elements.check_uncheck_checkbox_by_name(checkbox, check=True)
    selected_checkboxes = elements.get_you_have_selected_checkboxes()
    names_for_comparison = elements.checkboxes_name_for_you_have_selected_checkboxes(checkboxes_names)
    assert selected_checkboxes == names_for_comparison, f'Checkbox names selected -> {selected_checkboxes} do " \
                                                             f"not correspond to the names in "You have selected : ' \
                                                        f'<checkbox_name>, <checkbox_name>" block ' \
                                                        f'-> {names_for_comparison}'


def test_collapse_tree(home_page_get, get_elements_item):
    """
     Description: test checks that checked checkboxes names are in block
     "You have selected : <checkbox_name>, <checkbox_name>"

     Pre-conditions:
     1. Open browser
     2. Navigate to main page
     3. Navigate to page "Elements"
     4. Select menu item "Check box", press "Expand All" button [+]

     Steps:
     1. Press "Collapse All" button [-]
     2. Check that state of checkbox tree is collapsed

     Expected:
     1. After collapsing checkbox tree its state eq to False (i.e., it's collapsed)
     """
    elements = get_elements_item(bar_menu_check_box)
    elements.expand_all()
    elements.collapse_all()
    tree_state = elements.verify_tree_expanded_collapsed()
    assert tree_state == False, f"Checkbox tree should be collapsed with state False but" \
                                f" it's state is {tree_state}"
