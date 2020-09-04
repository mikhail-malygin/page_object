from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from .locators import ProductPageLocators
import math


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

    ''' Check login link: 
        - "is_login_page_login_form_present"
        - "is_login_page_register_form_present" 
    '''
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

    ''' Check product page: 
        - "is_product_page_url_present"
        - "is_product_page_name_present" 
        -" is_product_page_price_present"
        - "is_element_present" 
    '''
    def is_product_page_url_present(self, valid_substring_product_page_url):
        product_page_url = self.browser.current_url
        substring_product_page_url = product_page_url[product_page_url.index(ProductPageLocators.FIRST_ATTRIBUTE_OF_URL_PRODUCT_PAGE): len(product_page_url)]
        if substring_product_page_url == valid_substring_product_page_url:
            return True
        else:
            return False

    def is_product_page_name_present(self, how, what, valid_product_name):
        product_name = self.browser.find_element(how, what).text
        if product_name == valid_product_name:
            return True
        else:
            return False

    def is_product_page_price_present(self, how, what, valid_product_price):
        product_price = self.browser.find_element(how, what).text
        if product_price == valid_product_price:
            return True
        else:
            return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    ''' Check promo-codes when you add a product in the basket: 
                - "is_product_names_in_basket_and_in_product_page_the_same"
                - "is_product_prices_in_basket_and_in_product_page_the_same"           
    '''
    def is_product_names_in_basket_and_in_product_page_the_same(self, how, what, valid_product_name):
        product_name = self.browser.find_element(how, what).text
        if product_name == valid_product_name:
            return True
        else:
            return False

    def is_product_prices_in_basket_and_in_product_page_the_same(self, how, what, valid_product_price):
        product_price = self.browser.find_element(how, what).text
        if product_price == valid_product_price:
            return True
        else:
            return False
