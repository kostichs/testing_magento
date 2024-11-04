from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://magento.softwaretestingboard.com/'
        self.page_url = None

    def open_page(self):
        if self.page_url:
            self.browser.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError(f'Page {self.base_url}{self.page_url} cannot be opened')

    def find(self, locator):
        return self.browser.find_element(*locator)

    @staticmethod
    def find_in(web_element: WebElement, locator):
        return web_element.find_element(*locator)

    def find_all(self, locator):
        return self.browser.find_elements(*locator)

    @staticmethod
    def find_all_in(web_element: WebElement, locator):
        return web_element.find_elements(*locator)
