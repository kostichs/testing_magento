import random
import re
import time

from selenium.webdriver.support.ui import Select
import testing_magento.pages.locators.collections_page_loc as loc
from testing_magento.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from testing_magento.utils.sort_option import SortOption


class CollectionsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_url = '/collections/eco-friendly.html'

    def take_a_random_product(self):
        products = self.take_a_list_of_items()
        product = random.choice(products)
        product_name = self.find_in(product, loc.product_name_loc).text.strip()
        product_price = self.find_in(product, loc.product_price_loc).text.strip()
        return {
            'element': product,
            'name': product_name,
            'price': product_price
        }

    def take_a_list_of_items(self):
        return self.find_all(loc.products_loc)

    def __add_random_size(self, product):
        sizes = self.find_all_in(product, loc.product_sizes)
        random.choice(sizes).click()

    def __add_random_color(self, product):
        colors = self.find_all_in(product, loc.product_colors)
        random.choice(colors).click()

    def get_count(self):
        initial_count_text = self.find(loc.page_cart_counter_loc).text
        return int(initial_count_text) if initial_count_text.isdigit() else 0

    def add_to_cart(self, size_and_colors=True):
        initial_count = self.get_count()
        random_product_info = self.take_a_random_product()
        random_product = random_product_info['element']
        product_name = random_product_info['name']
        product_price = random_product_info['price']

        if size_and_colors:
            self.__add_random_size(random_product)
            self.__add_random_color(random_product)

        add_to_cart_button = self.find_in(random_product, loc.add_to_cart_button_loc)
        actions = ActionChains(self.browser)
        actions.move_to_element(random_product).click(add_to_cart_button).perform()

        if size_and_colors:
            WebDriverWait(self.browser, 10).until(
                lambda browser: self.get_count() > initial_count
            )
            cart_button = self.find(loc.page_cart_button_loc)
            cart_button.click()
            assert self.__verify_product_in_cart(product_name, product_price), f"Wrong product was added {product_name}"
        else:
            WebDriverWait(self.browser, 10).until(
                ec.visibility_of_element_located(loc.alert_message)
            )
            message_text = self.find(loc.alert_message).text
            assert message_text == 'You need to choose options for your item.', f"Alert message is wrong: {message_text}"

    def __verify_product_in_cart(self, product_name, product_price):
        WebDriverWait(self.browser, 10).until(
            ec.visibility_of_element_located(loc.cart_info_window_loc)
        )
        cart_data_block = self.find(loc.cart_data_block_loc)
        cart_name = self.find_in(cart_data_block, loc.inside_cart_product_name_loc).text.strip()
        cart_price = self.find_in(cart_data_block, loc.inside_cart_product_price_loc).text.strip()

        if cart_name == product_name and cart_price == product_price:
            print(f"Product matched: {cart_name}, Price: {cart_price}")
            return True
        print("No matching product found in the cart.")
        return False

    def switch_sorter_to(self, sort_option: SortOption):
        while True:
            sort_dropdown = self.browser.find_element(By.ID, "sorter")
            sort_select = Select(sort_dropdown)
            if sort_select.first_selected_option.get_attribute("value") != sort_option.value:
                sort_select.select_by_value(sort_option.value)
            else:
                break
        return sort_select

    def __get_all_prices(self):
        all_products = self.take_a_list_of_items()
        product_prices = []
        for product in all_products:
            price_text = self.find_in(product, loc.product_price_loc).text.strip()
            price = float(re.sub(r"[^\d.]", "", price_text))
            product_prices.append(price)
        return product_prices

    def sort_by_price(self):
        sort_select = self.switch_sorter_to(SortOption.PRICE)
        selected_option = sort_select.first_selected_option.get_attribute("value")
        assert selected_option == SortOption.PRICE.value, f"Wrong dropdown point selected: {selected_option}"

        WebDriverWait(self.browser, 10).until(
            ec.presence_of_all_elements_located(loc.products_loc)
        )
        prices = self.__get_all_prices()
        assert prices == sorted(prices), "Products are not sorted by price in ascending order"


        descending_button = self.find(loc.descend_ascend_button_loc)
        descending_button.click()

        WebDriverWait(self.browser, 10).until(
            ec.presence_of_all_elements_located(loc.products_loc)
        )
        
        prices = self.__get_all_prices()
        assert prices == sorted(prices, reverse=True), "Products are not sorted by price in descending order"
