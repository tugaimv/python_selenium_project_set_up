import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture()
def browser(request):
    language = request.config.getoption('language')
    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=option)
    yield browser
    browser.quit()
