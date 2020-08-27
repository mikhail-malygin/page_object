from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    def should_be_product_page(self, counter):
        self.should_be_product_page_url(counter)
        self.should_be_product_title(counter)
        self.should_be_product_price(counter)
        self.should_be_product_button_add_to_basket()

    def should_be_product_page_url(self, counter):
        assert self.SUBSTRING_PRODUCT_URL[counter] in self.browser.current_url, "The wrong url product page"

    def should_be_product_title(self, counter):
        assert self.is_product_page_title_present(*ProductPageLocators.NAME_FORM, counter), "The wrong product title"

    def should_be_product_price(self, counter):
        assert self.is_product_page_price_present(*ProductPageLocators.PRICE_FORM, counter), "The wrong product price"

    def should_be_product_button_add_to_basket(self):
        assert self.is_product_page_button_add_to_basket_present(*ProductPageLocators.BASKET_FORM), "The button " \
                                                                                                    "'Add to basket'" \
                                                                                                    " isn't available"

    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()
