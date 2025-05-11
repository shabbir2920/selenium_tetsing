import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.support_method import random_email_generator, random_password_generator

def test_happy_path_create_account(create_webdriver):
    """This test will open the website and create account of user"""
    driver = create_webdriver
    wait = WebDriverWait(driver, 20)
    login_locator = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Mnd902 KZnnKM tKTPp2"]')))
    login_locator.click()
    login_locator_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="login-modal-email-button"]')))
    login_locator_2.click()
    email_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
    email_locator.send_keys(random_email_generator())
    driver.find_element(By.XPATH, "//button[@data-testid='login-next-button']").click()
    password_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
    password_locator.send_keys(random_password_generator())
    driver.find_element(By.XPATH, "//button[text()='Create account']").click()
    skip_Setting = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Maybe later']")))
    skip_Setting.click()
    account = wait.until(EC.element_to_be_clickable
                         ((By.XPATH, "//div[@data-testid='desktop-dropdown-menu']/descendant::span")))
    action = ActionChains(driver)
    action.move_to_element(account).perform()
    logout = driver.find_element(By.XPATH, "//button[@data-testid='profile-menu-logout']/child::span[2]")
    assert logout.text == "Log out", f"test failed as account not created"




