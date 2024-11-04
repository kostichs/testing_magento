import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from testing_magento.pages.sale_page import SalePage
from testing_magento.pages.account_creation_page import CreationAccount
from testing_magento.pages.collections_page import CollectionsPage


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--force-device-scale-factor=0.5')
    #  options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(4)
    return browser


@pytest.fixture()
def create_account_page(browser):
    return CreationAccount(browser)


@pytest.fixture()
def collections_eco_page(browser):
    return CollectionsPage(browser)


@pytest.fixture()
def sale_page(browser):
    return SalePage(browser)
