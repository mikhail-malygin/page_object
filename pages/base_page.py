from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
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

    def is_product_page_button_add_to_basket_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

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
