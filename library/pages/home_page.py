from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    URL = "https://www.trivago.in/"

    LOGIN_BANNER_CTA = (By.XPATH, '//button[@data-testid="login-banner-cta"]')
    LOGIN_MODAL_EMAIL_BUTTON = (By.XPATH, '//button[@data-testid="login-modal-email-button"]')

    def open(self):
        self.driver.get(self.URL)

    def click_login_banner(self):
        self.click(*self.LOGIN_BANNER_CTA)

    def click_email_login(self):
        self.click(*self.LOGIN_MODAL_EMAIL_BUTTON)
