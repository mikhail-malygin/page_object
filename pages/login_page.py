from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage, LoginPageLocators):
    def __init__(self, browser, link, timeout=10):
        super().__init__(browser, link, timeout)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.SUBSTRING_LOGIN_URL in self.browser.current_url, "The wrong url login page"

    def should_be_login_form(self):
        assert self.is_login_page_login_form_present(*LoginPageLocators.LOGIN_FORM), "There is no a login form"

    def should_be_register_form(self):
        assert self.is_login_page_register_form_present(*LoginPageLocators.REGISTER_FORM), "There is no a register form"

    def register_new_user(self, email, password):
        input_email_address = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_ADDRESS_REGISTER_FORM)
        input_email_address.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REGISTER_FORM)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.INPUT_CONFIRM_PASSWORD_REGISTER_FORM)
        input_confirm_password.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_FORM)
        button_register.click()
