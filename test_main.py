import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure

LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "nellycdvm@gmail.com"
PASSWORD = "19942310nm!"
NEW_PASSWORD = "19942310nm!"

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.feature('Login Feature')
@allure.story('Invalid Login Attempt')
@allure.title('Test Invalid Login')
@allure.description('Test the system with invalid login credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("Test for invalid login credentials.")
def test_invalid_login(driver):
    driver.get(LOGIN_URL)
    with allure.step("Enter invalid email"):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@gmail.com")
    with allure.step("Enter invalid password"):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys("invalidpassword")
    with allure.step("Click login button"):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()
    time.sleep(3)
    with allure.step("Verify error message"):
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "Please wait and try again later" in error_message.text

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Login Feature')
@allure.story('Valid Login Attempt')
@allure.title('Test Valid Login')
@allure.description('Test the system with valid login credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("Test for valid login credentials.")
def test_login(driver):
    driver.get(LOGIN_URL)
    with allure.step("Enter valid email"):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(EMAIL)
    with allure.step("Enter valid password"):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(PASSWORD)
    with allure.step("Click login button"):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()
    time.sleep(3)
    with allure.step("Verify successful login"):
        assert driver.current_url == ACCOUNT_URL

@allure.feature('Change Password Feature')
@allure.story('Change Password with Incorrect Current Password')
@allure.title('Test Change Password with Incorrect Current Password')
@allure.description('Test changing password with incorrect current password')
@allure.severity(allure.severity_level.NORMAL)
@allure.step("Test changing password with incorrect current password.")
def test_change_password_incorrect_current(driver):
    driver.get(ACCOUNT_URL)
    with allure.step("Navigate to change password page"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()
    with allure.step("Enter incorrect current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")
    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)
    with allure.step("Confirm new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)
    with allure.step("Save new password"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()
    time.sleep(3)
    with allure.step("Verify error message for incorrect current password"):
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "The password doesn't match this account." in error_message.text

@allure.feature('Change Password Feature')
@allure.story('Change Password with Mismatched Confirmation')
@allure.title('Test Change Password with Mismatched Confirmation')
@allure.description('Test changing password with mismatched confirmation password')
@allure.severity(allure.severity_level.NORMAL)
@allure.step("Test changing password with mismatched confirmation.")
def test_change_password_mismatch(driver):
    driver.get(ACCOUNT_URL)
    with allure.step("Navigate to change password page"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()
    with allure.step("Enter current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)
    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)
    with allure.step("Enter mismatched confirmation password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("mismatchedpassword")
    with allure.step("Save new password"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()
    time.sleep(3)
    with allure.step("Verify error message for mismatched confirmation"):
        error_message = driver.find_element(By.ID, "password-confirmation-error")
        assert "Please enter the same value again." in error_message.text

@allure.feature('Change Password Feature')
@allure.story('Successful Password Change')
@allure.title('Test Successful Password Change')
@allure.description('Test successful password change')
@allure.severity(allure.severity_level.CRITICAL)
@allure.step("Test successful password change.")
def test_change_password(driver):
    driver.get(ACCOUNT_URL)
    with allure.step("Navigate to change password page"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()
    with allure.step("Enter current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)
    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)
    with allure.step("Confirm new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)
    with allure.step("Save new password"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()
    with allure.step("Verify successful password change message"):
        success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")
        assert "You saved the account information." in success_message.text
