from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, by, locator):
        """Wait until element is clickable and return it."""
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click(self, by, locator):
        el = self.find(by, locator)
        el.click()

    def send_keys(self, by, locator, text: str):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def open(self, url: str):
        self.driver.get(url)
