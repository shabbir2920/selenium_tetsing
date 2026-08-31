import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.support_method import random_email_generator, random_password_generator
from library.pages.home_page import HomePage
from library.pages.login_page import LoginPage
from library.pages.account_page import AccountPage


def test_happy_path_create_account(create_webdriver):
    """This test will open the website and create account of user
    steps
    1: click on create account button
    2. enter the email address created using faker
    3. enter the password created using faker
    4. click on submit button"""
    driver = create_webdriver
    # Use page objects
    home = HomePage(driver)
    login = LoginPage(driver)
    account = AccountPage(driver)

    # Open home (conftest already opens, but calling open is idempotent)
    home.open()

    # Navigate to login / create flow
    home.click_login_banner()
    home.click_email_login()

    email = random_email_generator()
    login.enter_email(email)
    login.click_next()

    password = random_password_generator()
    login.enter_password(password)
    login.click_create_account()

    # Wait a moment for account creation flow to finish and skip settings
    time.sleep(5)
    account.skip_settings()

    # Hover over account and assert logout is present
    account.hover_account()
    logout_text = account.get_logout_text()
    assert logout_text == "Log out", "test failed as account not created"


def test_happy_path_login_account(create_webdriver):
    """Placeholder for login test using saved credentials in credentials/.

    Implementers can read credentials/username.txt and credentials/password.txt
    and drive the login path using the same page objects. Kept separate so account
    creation and login responsibilities are isolated.
    """
    pass
