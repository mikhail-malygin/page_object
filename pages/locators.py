from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators:
    SUBSTRING_LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_ADDRESS_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REGISTER_FORM = (By.CSS_SELECTOR, "div #id_registration-password1")
    INPUT_CONFIRM_PASSWORD_REGISTER_FORM = (By.CSS_SELECTOR, "div #id_registration-password2")
    TEST_EMAIL = "test_malygin@gmail.com"
    TEST_PASSWORD = "qwerty123"


class ProductPageLocators:
    # Product attributes: page_url, substring_page_url, name, price
    PRODUCT_THE_SHELLCODERS_HANDBOOK = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders"
                                        "-handbook_209/?promo=newYear",
                                        "catalogue/the-shellcoders-handbook_209/?promo=newYear",
                                        "The shellcoder's handbook", "£9.99")
    PRODUCT_CODERS_AT_WORK = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                              "catalogue/coders-at-work_207/?promo=newYear2019", "Coders at Work", "£19.99")
    PRODUCT_THE_CITY_AND_THE_STARS = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95",
                                      "catalogue/the-city-and-the-stars_95", "the-city-and-the-stars_95", "£16.99")
    FIRST_ATTRIBUTE_OF_URL_PRODUCT_PAGE = "catalogue"
    # Selectors of the product page
    NAME_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_FORM = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class ProductPagePromo:
    PRODUCT_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


class BasketPageLocators:
    BASKET_LINK = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    # Selectors of the basket page and message about adding the product in the basket
    IN_MESSAGE_ADD_TO_BASKET_FORM_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    IN_MESSAGE_ADD_TO_BASKET_FORM_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    VIEW_BASKET_BUTTON_FORM = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > "
                                                "div > p:nth-child(2) > a:nth-child(1)")
    BASKET_NAME_FORM = (By.CSS_SELECTOR, "div .col-sm-4 [href='/en-gb/catalogue/coders-at-work_207/']")
    BASKET_PRICE_FORM = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-1 > p")
    BASKET_IS_EMPTY_FORM = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    BASKET_IS_EMPTY_MESSAGE_FORM = (By.CSS_SELECTOR, "#content_inner > p")
