from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators


class BasePage(ProductPageLocators):
    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_login_page_login_form_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_login_page_register_form_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_product_page_title_present(self, how, what):
        title = self.browser.find_element(how, what).text
        if title == ProductPageLocators.PRODUCT_NAME:
            return True
        else:
            return False

    def is_product_page_price_present(self, how, what):
        price = self.browser.find_element(how, what).text
        if price == ProductPageLocators.PRODUCT_PRICE:
            return True
        else:
            return False

    def is_product_page_button_add_to_busket_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
