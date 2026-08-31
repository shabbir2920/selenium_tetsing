from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    NEXT_BUTTON = (By.XPATH, "//button[@data-testid='login-next-button']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Create account']")

    def enter_email(self, email: str):
        self.send_keys(*self.EMAIL_INPUT, email)

    def click_next(self):
        self.click(*self.NEXT_BUTTON)

    def enter_password(self, password: str):
        self.send_keys(*self.PASSWORD_INPUT, password)

    def click_create_account(self):
        self.click(*self.CREATE_ACCOUNT_BUTTON)
