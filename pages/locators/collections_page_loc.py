from selenium.webdriver.common.by import By

products_table_loc = (By.CSS_SELECTOR, ".products.wrapper.grid.products-grid")
products_loc = (By.CSS_SELECTOR, ".item.product.product-item")
product_name_loc = (By.CSS_SELECTOR, ".product-item-link")
product_price_loc = (By.CSS_SELECTOR, ".price-wrapper .price")
product_sizes = (By.CSS_SELECTOR, ".swatch-attribute-options .swatch-option.text")
product_colors = (By.CSS_SELECTOR, ".swatch-attribute-options .swatch-option.color")

add_to_cart_button_loc = (By.CSS_SELECTOR, 'button.action.tocart')
page_cart_button_loc = (By.CSS_SELECTOR, 'a.action.showcart')
page_cart_counter_loc = (By.CSS_SELECTOR, 'a.action.showcart .counter-number')
inside_cart_product_name_loc = (By.CSS_SELECTOR, 'li.item.product.product-item .product-item-name a')
inside_cart_product_price_loc = (By.CSS_SELECTOR, 'li.item.product.product-item .price-wrapper .price')
inside_cart_product_qty_loc = (By.CSS_SELECTOR, 'li.item.product.product-item .item-qty')
cart_info_window_loc = (By.CSS_SELECTOR, '.block.block-minicart')
cart_data_block_loc = (By.CSS_SELECTOR, '.minicart-wrapper.active')

dropdown_sorter_loc = (By.ID, "sorter")
descend_ascend_button_loc = (By.CSS_SELECTOR, "a.action.sorter-action.sort-asc")

#  opens in the separate page of the product
alert_message = (By.CSS_SELECTOR, 'div[role="alert"] .message-notice div')
