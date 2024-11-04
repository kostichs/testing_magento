import random
import testing_magento.pages.locators.sale_page_loc as loc
from testing_magento.pages.basepage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SalePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = '/sale.html'

    def open_random_link(self):
        links = self.find_all(loc.links_loc)
        while True:
            random_link = random.choice(links)
            href = random_link.get_attribute("href")
            if href:
                break

        self.browser.execute_script("window.open(arguments[0], '_blank');", href)
        yield
        self.browser.close()

    def open_all_sale_offers(self):
        try:
            links = self.find(loc.links_loc)
            for link in links:
                href = link.get_attribute("href")
                if href:
                    self.browser.execute_script("window.open(arguments[0], '_blank');", href)
                    self.browser.switch_to.window(self.browser.window_handles[-1])

                    WebDriverWait(self.browser, 10).until(
                        ec.visibility_of_element_located(loc.page_title_wrapper_loc))
                    title_element = self.find(loc.page_title_heading_loc)

                    href_part = href.split('/')[-1].replace('.html', '')
                    href_word_part = href_part.split('-')[0]
                    title_text = title_element.text

                    #  print(title_text, href_word_part)
                    assert href_word_part.lower() in title_text.lower(), f'{title_text} does not match for: {href}'

                    self.browser.close()
                    self.browser.switch_to.window(self.browser.window_handles[0])

        except Exception as e:
            print(f"An error occurred: {e}")

    def find_label(self):
        self.open_random_link()
        label_element = self.find(loc.google_label_loc)
        label_text = label_element.text
        print(label_text)
        assert label_element.is_displayed(), "Label does not appear on the page"

    def check_title(self):
        page_heading = self.find(loc.page_title_heading_loc).text
        page_title = self.browser.title
        assert page_title == page_heading, f"Title {page_title} does not match to heading {page_heading}"
