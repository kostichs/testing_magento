import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from testing_magento.pages.sale_page import SalePage
from testing_magento.pages.account_creation_page import CreationAccount
from testing_magento.pages.collections_page import CollectionsPage
import allure


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--force-device-scale-factor=0.5')
    options.add_argument('--headless')
    #  options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(4)
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@pytest.fixture()
def create_account_page(browser):
    return CreationAccount(browser)


@pytest.fixture()
def collections_eco_page(browser):
    return CollectionsPage(browser)


@pytest.fixture()
def sale_page(browser):
    return SalePage(browser)
