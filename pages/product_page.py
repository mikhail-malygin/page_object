from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators, BasePageLocators


class ProductPage(BasePage, ProductPageLocators):
    def __init__(self, browser, link, timeout=10):
        super().__init__(browser, link, timeout)
        self.basket_price = None

    def should_be_product_page(self, valid_substring_product_page_url, valid_product_name, valid_product_price):
        self.should_be_product_page_url(valid_substring_product_page_url)
        self.should_be_product_name(valid_product_name)
        self.should_be_product_price(valid_product_price)
        self.should_be_product_button_add_to_basket()

    def should_be_product_page_url(self, valid_substring_product_page_url):
        assert self.is_product_page_url_present(valid_substring_product_page_url), "The wrong url product page"

    def should_be_product_name(self, valid_product_name):
        assert self.is_product_page_name_present(*ProductPageLocators.NAME_FORM, valid_product_name), \
            "The wrong product title"

    def should_be_product_price(self, valid_product_price):
        assert self.is_product_page_price_present(*ProductPageLocators.PRICE_FORM, valid_product_price), \
            "The wrong product price"

    def should_be_product_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_FORM), "The button 'Add to basket' isn't available"

    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()

    def open_busket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def check_the_product_name_in_message(self, valid_product_name):
        assert self.is_product_names_in_basket_and_in_product_page_the_same \
            (*BasketPageLocators.IN_MESSAGE_ADD_TO_BASKET_FORM_PRODUCT_NAME, valid_product_name), \
            "The product names in the product page and in the basket page are different"

    def check_the_product_price_in_message(self, valid_product_price):
        assert self.is_product_prices_in_basket_and_in_product_page_the_same \
            (*BasketPageLocators.IN_MESSAGE_ADD_TO_BASKET_FORM_PRODUCT_PRICE, valid_product_price), \
            "The product prices in the product page and in the basket page are different"

    def should_be_button_view_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.VIEW_BASKET_BUTTON_FORM), "The button 'View basket' isn't available"

    def view_basket(self):
        view_basket_button = self.browser.find_element(*BasketPageLocators.VIEW_BASKET_BUTTON_FORM)
        view_basket_button.click()

    def check_the_product_name_and_in_the_basket(self, valid_product_name):
        assert self.is_product_names_in_basket_and_in_product_page_the_same \
            (*BasketPageLocators.BASKET_NAME_FORM, valid_product_name), \
            "The product names in the product page and in the basket page are different"

    def check_the_product_price_and_in_the_basket(self, valid_product_price):
        assert self.is_product_prices_in_basket_and_in_product_page_the_same \
            (*BasketPageLocators.BASKET_PRICE_FORM, valid_product_price), \
            "The product names in the product page and in the basket page are different"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def there_is_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is a success message"

    def message_should_be_disapperead(self):
        assert self.element_is_disapperead(*ProductPageLocators.SUCCESS_MESSAGE), "Success message isn't disappeared"
