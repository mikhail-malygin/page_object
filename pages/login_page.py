from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
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
