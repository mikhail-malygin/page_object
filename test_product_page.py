import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.parametrize("link, valid_substring_product_page_url, product_name, product_price",
                         [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK,
                          ProductPageLocators.PRODUCT_CODERS_AT_WORK])
def test_guest_can_see_product_page(browser, link, valid_substring_product_page_url, product_name, product_price):
    # Go to a product page.
    # Check necessary attributes of the product page: valid url product page, presence name and price of product
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(valid_substring_product_page_url, product_name, product_price)


@pytest.mark.parametrize("link, valid_substring_product_page_url, product_name, product_price",
                         [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK,
                          ProductPageLocators.PRODUCT_CODERS_AT_WORK])
def test_guest_can_add_product_to_basket(browser, link, valid_substring_product_page_url, product_name, product_price):
    # Check to add a product to the basket. Also solve a quiz by the Stepik course
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(valid_substring_product_page_url, product_name, product_price)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()


@pytest.mark.parametrize("link", [pytest.param(ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK[0],
                                               marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize("link", [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK[0]])
def test_guest_cant_see_success_message(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.there_is_no_success_message()


@pytest.mark.parametrize("link", [pytest.param(ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK[0],
                                               marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.message_should_be_disapperead()


def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.PRODUCT_THE_CITY_AND_THE_STARS[0]
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_THE_CITY_AND_THE_STARS[0]
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
