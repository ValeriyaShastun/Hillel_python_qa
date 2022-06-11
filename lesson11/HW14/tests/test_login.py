import logging
import time
import pytest
from selenium.webdriver.common.by import By

logger = logging.getLogger()
logger.setLevel('INFO')

username = "valeriia_is_here"
password = "valeriiatest"
login_url = "http://www.testyou.in/Login.aspx?ReturnUrl=%2fStudent%2fStudentIndex.aspx"
home_page_url = "http://www.testyou.in/Student/StudentIndex.aspx"
username_selector = '[name$="Container$txtUserLogin"]'
password_selector = '[name$="Container$txtPassword"]'
login_button_selector = '[type="submit"][name$="btnLoginn"]'

@pytest.mark.positive
def test_login_chrome_success(chrome_driver):
    """
    Description: test opens chrome browser, inserts login, password, presses button [Login],
    checks that url has changed for homepage url

    Pre-conditions:
    1. Open chrome browser

    Steps:
    1. Insert correct Login
    2. Insert correct password
    3. Press [Login] button
    4. Check that url has changed for homepage url

    Expected:
    1. User logged in successfully using chrome browser and he is on the Home page
    """
    driver = chrome_driver
    driver.maximize_window()
    driver.get(login_url)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, username_selector).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_button_selector).click()
    time.sleep(5)
    assert driver.current_url == home_page_url


@pytest.mark.positive
def test_login_firefox_success(firefox_driver):
    """
    Description: test opens firefox browser, inserts login, password, presses button [Login],
    checks that url has changed for homepage url

    Pre-conditions:
    1. Open firefox browser

    Steps:
    1. Insert correct Login
    2. Insert correct password
    3. Press [Login] button
    4. Check that url has changed for homepage url

    Expected:
    1. User logged in successfully using firefox browser and he is on the Home page
    """
    driver = firefox_driver
    driver.maximize_window()
    driver.get(login_url)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, username_selector).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_button_selector).click()
    time.sleep(5)
    assert driver.current_url == home_page_url


@pytest.mark.positive
def test_login_edge_success(edge_driver):
    """
    Description: test opens edge browser, inserts login, password, presses button [Login],
    checks that url has changed for homepage url

    Pre-conditions:
    1. Open edge browser

    Steps:
    1. Insert correct Login
    2. Insert correct password
    3. Press [Login] button
    4. Check that url has changed for homepage url

    Expected:
    1. User logged in successfully using edge browser and he is on the Home page
    """
    driver = edge_driver
    driver.maximize_window()
    driver.get(login_url)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, username_selector).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_button_selector).click()
    time.sleep(5)
    assert driver.current_url == home_page_url
