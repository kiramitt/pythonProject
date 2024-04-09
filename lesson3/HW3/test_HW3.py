import time
from locators import *
from assert_messages import *
from selenium.webdriver.support import expected_conditions as EC


# Необходимо написать 3 автотеста для данной страницы:
# С использованием Explicit waits и Expected Conditions
def test_registration_functionality_with_explicit_waits(driver, wait):
    driver.get(main_url)
    assert driver.find_element(*head_title).text == expected_head_title, assert_head_title
    wait.until(EC.element_to_be_clickable(driver.find_element(*start_test_button))).click()
    driver.find_element(*login_field).send_keys(login)
    driver.find_element(*password_field).send_keys(password)
    checkbox_agree = driver.find_element(*agree_checkbox)
    checkbox_agree.click()
    assert checkbox_agree.is_selected()
    driver.find_element(*register_button).click()
    assert check_exists(driver, loader), assert_loader_exist
    wait.until(EC.visibility_of_element_located(success_message))
    assert (check_exists(driver, success_message) and
            driver.find_element(*success_message).text == expected_success_message and
            not check_exists(driver, loader)), assert_success_message


# С использованием Implicit waits
def test_registration_functionality_with_implicit_waits(browser):
    browser.get(main_url)
    assert browser.find_element(*head_title).text == expected_head_title, assert_head_title
    browser.find_element(*start_test_button).click()
    browser.find_element(*login_field).send_keys(login)
    browser.find_element(*password_field).send_keys(password)
    checkbox_agree = browser.find_element(*agree_checkbox)
    checkbox_agree.click()
    assert checkbox_agree.is_selected()
    browser.find_element(*register_button).click()
    assert check_exists(browser, loader), assert_loader_exist
    time.sleep(4)
    assert (check_exists(browser, success_message) and
            browser.find_element(*success_message).text == expected_success_message and
            not check_exists(browser, loader)), assert_success_message


# С использованием time.sleep()
def test_registration_functionality_with_time_sleep(driver):
    driver.get(main_url)
    assert driver.find_element(*head_title).text == expected_head_title, assert_head_title
    time.sleep(5)
    driver.find_element(*start_test_button).click()
    driver.find_element(*login_field).send_keys(login)
    driver.find_element(*password_field).send_keys(password)
    checkbox_agree = driver.find_element(*agree_checkbox)
    checkbox_agree.click()
    assert checkbox_agree.is_selected()
    driver.find_element(*register_button).click()
    assert check_exists(driver, loader), assert_loader_exist
    time.sleep(4)
    assert (driver.find_element(*success_message).text == expected_success_message and
            not check_exists(driver, loader)), assert_success_message


# Так же необходимо написать несколько автотестов для сайта https://the-internet.herokuapp.com/ опираясь на
# полученные знания и поиск в интернете новой информации.
# https://the-internet.herokuapp.com/add_remove_elements/ (Необходимо создать и удалить элемент)
def test_add_delete_element(browser):
    browser.get(add_delete_element_url)


# https://the-internet.herokuapp.com/basic_auth
def test_basic_auth(browser):
    browser.get(basic_auth_url)


# https://the-internet.herokuapp.com/broken_images (Необходимо найти сломанные изображения)
def test_broken_images(browser):
    browser.get(broken_images_url)


# https://the-internet.herokuapp.com/checkboxes (Практика с чек боксами)
def test_checkboxes(browser):
    browser.get(checkboxes_url)
