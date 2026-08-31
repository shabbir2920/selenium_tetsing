from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from .base_page import BasePage

class AccountPage(BasePage):
    SKIP_SETTINGS_BUTTON = (By.XPATH, "//button[@class='ehv1KY tjDLq2 Gp_pWr']")
    DESKTOP_DROPDOWN = (By.XPATH, "//div[@data-testid='desktop-dropdown-menu']/descendant::span")
    LOGOUT_BUTTON = (By.XPATH, "//button[@data-testid='profile-menu-logout']/descendant::span[3]")

    def skip_settings(self):
        self.click(*self.SKIP_SETTINGS_BUTTON)

    def hover_account(self):
        account = self.wait.until(EC.element_to_be_clickable(self.DESKTOP_DROPDOWN))
        ActionChains(self.driver).move_to_element(account).perform()

    def get_logout_text(self):
        logout = self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
        return logout.text
