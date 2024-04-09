from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


def check_exists(browser, selector):
    try:
        element = browser.find_element(*selector)
        return element.is_displayed()
    except NoSuchElementException:
        return False


# HEADER
head_title = (By.CSS_SELECTOR, "body > h1")
start_test_button = (By.ID, "startTest")

# REGISTRATION
login_field = (By.ID, "login")
password_field = (By.ID, "password")
agree_checkbox = (By.ID, "agree")
register_button = (By.ID, "register")

loader = (By.ID, "loader")

success_message = (By.ID, "successMessage")
