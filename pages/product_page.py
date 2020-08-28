from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    def should_be_product_page(self, substring_product_page_url, product_name, product_price):
        self.should_be_product_page_url(substring_product_page_url)
        self.should_be_product_name(product_name)
        self.should_be_product_price(product_price)
        self.should_be_product_button_add_to_basket()

    def should_be_product_page_url(self, substring_product_page_url):
        assert substring_product_page_url in self.browser.current_url, "The wrong url product page"

    def should_be_product_name(self, product_name):
        assert self.is_product_page_name_present(*ProductPageLocators.NAME_FORM, product_name), \
                                                                                               "The wrong product title"

    def should_be_product_price(self, product_price):
        assert self.is_product_page_price_present(*ProductPageLocators.PRICE_FORM, product_price), \
                                                                                               "The wrong product price"

    def should_be_product_button_add_to_basket(self):
        assert self.is_product_page_button_add_to_basket_present(*ProductPageLocators.BASKET_FORM), \
                                                                            "The button 'Add to basket' isn't available"

    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()
