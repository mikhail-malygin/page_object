from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    SUBSTRING_LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    # Product attributes: page_url, substring_page_url, name, price
    PRODUCT_THE_SHELLCODERS_HANDBOOK = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders"
                                        "-handbook_209/?promo=newYear",
                                        "the-shellcoders-handbook_209/?promo=newYear", "The shellcoder's handbook",
                                        "£9.99")
    PRODUCT_CODERS_AT_WORK = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                              "coders-at-work_207/?promo=newYear2019", "Coders at Work", "£19.99")
    # Selectors of the product page
    NAME_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form button")
