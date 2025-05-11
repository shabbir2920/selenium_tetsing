import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture(scope="session", autouse=True)
def create_webdriver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.trivago.in/")
    driver.maximize_window()
    time.sleep(2)
    print(f"{driver.title} website is open")

    yield driver
    driver.quit()


@pytest.hookimpl
def pytest_runtest_setup(item):
    print(f"{('_' * 30)} SETUP FOR - {item.name} {('_' * 30)}")


@pytest.hookimpl
def pytest_runtest_teardown(item):
    print(f"{('_' * 30)} COMPLETED TEST CASE EXECUTION - {item.name} {('_' * 30)}")
