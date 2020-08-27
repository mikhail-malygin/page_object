from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_be_product_title()
        self.should_be_product_price()
        self.should_be_product_button_add_to_basket()

    def should_be_product_page_url(self):
        assert self.SUBSTRING_PRODUCT_THE_SHELLCODERS_HANDBOOK_URL in self.browser.current_url, "The wrong url " \
                                                                                                "product page "

    def should_be_product_title(self):
        assert self.is_product_page_title_present(*ProductPageLocators.TITLE_FORM), "The wrong product title"

    def should_be_product_price(self):
        assert self.is_product_page_price_present(*ProductPageLocators.PRICE_FORM), "The wrong product price"

    def should_be_product_button_add_to_basket(self):
        assert self.is_product_page_button_add_to_basket_present(*ProductPageLocators.BASKET_FORM), "The button " \
                                                                                                    "'Add to basket'" \
                                                                                                    " isn't available"

    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()
