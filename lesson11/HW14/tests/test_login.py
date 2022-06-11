import logging
import time
import pytest
from selenium.webdriver.common.by import By

logger = logging.getLogger()
logger.setLevel('INFO')

@pytest.mark.positive
@pytest.mark.parametrize("browser", ["firefox", "chrome", "edge"])
def test_login_success(get_driver, browser):
    """
    Description: test opens browser, inserts login, password, presses button [Login],
    checks that url has changed for homepage url

    Pre-conditions:
    1. Open browser

    Steps:
    1. Insert correct Login
    2. Insert correct password
    3. Press [Login] button
    4. Check that url has changed for homepage url

    Expected:
    1. User logged in successfully and he is on the Home page
    """
    driver = get_driver(browser)
    username = "valeriia_is_here"
    password = "valeriiatest"
    login_url = "http://www.testyou.in/Login.aspx?ReturnUrl=%2fStudent%2fStudentIndex.aspx"
    home_page_url = "http://www.testyou.in/Student/StudentIndex.aspx"
    driver.get(login_url)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, '[name$="Container$txtUserLogin"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '[name$="Container$txtPassword"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"][name$="btnLoginn"]').click()
    time.sleep(5)
    assert driver.current_url == home_page_url
