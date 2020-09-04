import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPagePromo, ProductPageLocators


@pytest.mark.parametrize('promo_code', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_see_product_page(browser, promo_code):
    # Go to a product page basket using different promo codes. They are part of the product page url
    # Check necessary attributes of the product page: valid url product page, presence name and price of product
    link = ProductPagePromo.PRODUCT_PROMO + promo_code
    valid_substring_product_page_url = link[link.index(ProductPageLocators.FIRST_ATTRIBUTE_OF_URL_PRODUCT_PAGE): len(link)]
    valid_product_name = ProductPageLocators.PRODUCT_CODERS_AT_WORK[2]
    valid_product_price = ProductPageLocators.PRODUCT_CODERS_AT_WORK[3]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(valid_substring_product_page_url, valid_product_name, valid_product_price)


@pytest.mark.parametrize("promo_code", ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),
                                        "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_code):
    # Check to add a product to the basket using different promo codes
    link = ProductPagePromo.PRODUCT_PROMO + promo_code
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    valid_product_name = ProductPageLocators.PRODUCT_CODERS_AT_WORK[2]
    valid_product_price = ProductPageLocators.PRODUCT_CODERS_AT_WORK[3]
    product_page.check_the_product_name_in_message(valid_product_name)
    product_page.check_the_product_price_in_message(valid_product_price)
    product_page.should_be_button_view_basket()
    product_page.view_basket()
    product_page.check_the_product_name_and_in_the_basket(valid_product_name)
    product_page.check_the_product_price_and_in_the_basket(valid_product_price)
