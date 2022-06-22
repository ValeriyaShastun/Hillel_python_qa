from selenium.webdriver.common.by import By

# Represents all HTML selectors, each element include selector and select by type
elements_card = (By.XPATH, '//div[@class="card-body"]//h5[contains(text(), "Elements")]')
forms_card = (By.XPATH, '//div[@class="card-body"]//h5[contains(text(), "Forms")]')
alerts_frame_windows_card = (By.XPATH, '//div[@class="card-body"]//h5[contains(text(), "Alerts, Frame & Windows")]')
widgets_card = (By.XPATH, '//div[@class="card-body"]//h5[contains(text(), "Widgets")]')
interactions_card = (By.XPATH, '//div[@class="card-body"]//h5[contains(text(), "Interactions")]')
book_store_app = (By.XPATH, '//div[@class="card-body"]//h5[contains(text(), "Book Store Application")]')
