import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.parametrize("link, substring_product_page_url, product_name, product_price",
                         [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK,
                          ProductPageLocators.PRODUCT_CODERS_AT_WORK])
def test_guest_can_see_product_page(browser, link, substring_product_page_url, product_name, product_price):
    # Go to a product page.
    # Check necessary attributes of the product page: valid url product page, presence name and price of product
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(substring_product_page_url, product_name, product_price)


@pytest.mark.parametrize("link, substring_product_page_url, product_name, product_price",
                         [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK,
                          ProductPageLocators.PRODUCT_CODERS_AT_WORK])
def test_guest_can_add_product_to_basket(browser, link, substring_product_page_url, product_name, product_price):
    # Check to add a product to the basket. Also solve a quiz by the Stepik course
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(substring_product_page_url, product_name, product_price)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
