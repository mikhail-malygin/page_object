from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException


class BasePage:
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
