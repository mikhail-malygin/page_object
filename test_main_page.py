from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators, BasketPageLocators
from .pages.basket_page import BasketPage


def test_guest_should_see_login_link(browser):
    # Check a login link element on the main page
    link = MainPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_and_check_login_page(browser):
    # Go to a login page through the login link element.
    # Check necessary attributes of the login page: valid url login page, presence login form and register form
    link = MainPageLocators.MAIN_PAGE_URL
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Check necessary attributes of the empty basket
    link = MainPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.open_basket()
    basket_link = BasketPageLocators.BASKET_LINK
    basket_page = BasketPage(browser, basket_link)
    basket_page.basket_is_empty()
