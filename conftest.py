from selenium import webdriver
import pytest
import time


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default = "en", help="Choose ui language:")


@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    yield browser
    #time.sleep(30)
    browser.quit()
