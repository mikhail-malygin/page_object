from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    SUBSTRING_LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    SUBSTRING_PRODUCT_THE_SHELLCODERS_HANDBOOK_URL = "the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_NAME = "The shellcoder's handbook"
    TITLE_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE = "£9.99"
    PRICE_FORM = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    BUSKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form button1")
