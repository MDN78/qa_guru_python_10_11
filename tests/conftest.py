import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import project
import dotenv


@pytest.fixture(scope='function', autouse=True)
def driver_configuration():
    # dotenv.load_dotenv()
    # driver_options = webdriver.ChromeOptions()
    # driver_options.page_load_strategy = 'eager'
    # browser.config.driver_options = driver_options

    # options = Options()
    # options.page_load_strategy = 'eager'

    browser.config.driver_name = project.config.driver_name
    if browser.config.driver_name == 'firefox':
        options = Options()
        options.page_load_strategy = 'eager'
        browser.config.driver_options = options
    else:
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options
    browser.config.hold_driver_at_exit = project.config.hold_driver_at_exit
    # browser.config.window_width = project.config.window_width
    # browser.config.window_height = project.config.window_height
    browser.config.base_url = project.config.base_url
    browser.config.timeout = project.config.timeout

    yield

    browser.quit()
