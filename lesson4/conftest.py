import pytest
from selenium import webdriver
from lesson4.urls import base_url
from lesson4.pages.auth_page import LoginPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    print(f'\nStart test')
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    print("\nEnd test")


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver, base_url)
    return page
