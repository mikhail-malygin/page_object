from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    SUBSTRING_LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    LINK = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear ",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019")
    SUBSTRING_PRODUCT_URL = ("the-shellcoders-handbook_209/?promo=newYear", "coders-at-work_207/?promo=newYear2019")
    PRODUCT_NAME = ("The shellcoder's handbook", "Coders at Work")
    NAME_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE = ("£9.99", "£19.99")
    PRICE_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form button")
