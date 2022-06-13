import logging
import time
import pytest

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.mark.positive
def test_login_chrome_success(chrome_driver, generate_data_for_test, login):
    """
    Description: Login with correct credentials to website using Chrome browser,
    verify that login is successful

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
    logger.info("Start of test test_login_chrome_success")
    driver = chrome_driver
    logger.info("Chrome driver has been created")
    driver.maximize_window()
    data_for_test = generate_data_for_test
    driver.get(data_for_test["login_url"])
    time.sleep(4)
    login(driver, data_for_test)
    time.sleep(5)
    assert driver.current_url == data_for_test["home_page_url"]


@pytest.mark.positive
def test_login_firefox_success(firefox_driver, generate_data_for_test, login):
    """
    Description: Login with correct credentials to website using Firefox browser,
    verify that login is successful

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
    logger.info("Start of test test_login_firefox_success")
    driver = firefox_driver
    logger.info("Firefox driver has been created")
    driver.maximize_window()
    data_for_test = generate_data_for_test
    driver.get(data_for_test["login_url"])
    time.sleep(4)
    login(driver, data_for_test)
    time.sleep(5)
    assert driver.current_url == data_for_test["home_page_url"]


@pytest.mark.positive
def test_login_edge_success(edge_driver, generate_data_for_test, login):
    """
    Description: Login with correct credentials to website using Edge browser,
    verify that login is successful

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
    logger.info("Start of test test_login_edge_success")
    driver = edge_driver
    logger.info("Edge driver has been created")
    driver.maximize_window()
    data_for_test = generate_data_for_test
    driver.get(data_for_test["login_url"])
    time.sleep(4)
    login(driver, data_for_test)
    time.sleep(5)
    assert driver.current_url == data_for_test["home_page_url"]
