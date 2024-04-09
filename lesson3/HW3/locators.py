from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


def check_exists(browser, selector):
    try:
        browser.find_element(*selector)
    except NoSuchElementException:
        return False
    return True


# username_field = (By.ID, "user-name")
