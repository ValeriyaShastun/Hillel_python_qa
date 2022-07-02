from selenium.webdriver.common.by import By

# Represents all HTML selectors, each element include selector and select by type
menu_items = ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons", "Links", "Broken Links - Images",
              "Broken Links - Images", "Dynamic Properties"]
menu_item = [By.XPATH, '//span[contains(text(), "{}")]']

all_checkbox_names = ["Home", "Desktop", "Notes", "Commands", "Documents", "WorkSpace", "React", "Angular", "Veu",
                      "Office", "Public", "Private", "Classified", "General", "Downloads", "Word File.doc",
                      "Excel File.doc"]

expand_all_button = [By.XPATH, '//button[contains(@class, "rct-option-expand-all")]']
collapse_all_button = [By.XPATH, '//button[contains(@class, "rct-option-collapse-all")]']
tree_expanded = [
    By.XPATH, '//div[@id="tree-node"]/ol/li[contains(@class, "rct-node rct-node-parent rct-node-expanded")]']
checkbox = [By.CSS_SELECTOR, 'label[for*="tree-node-{}"] span[class="rct-checkbox"]']
checkbox_state = [By.CSS_SELECTOR, 'label[for*="tree-node-{}"] span[class="rct-checkbox"] svg']
checkboxes_state = [By.CSS_SELECTOR, 'label[for*="tree-node"] span[class="rct-checkbox"] svg']
you_have_selected_checkboxes_name = [By.CSS_SELECTOR, ".text-success"]
