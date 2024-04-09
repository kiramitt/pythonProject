import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser(request):
    print(f'\nStart test: {request.node.name}')
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print("\nEnd test")
