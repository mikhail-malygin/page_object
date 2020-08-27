from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_see_product_page(browser):
    for counter in range(len(ProductPageLocators.LINK)):
        link = ProductPageLocators.LINK[counter]
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page(counter)


def test_guest_can_add_product_to_basket(browser):
    for counter in range(len(ProductPageLocators.LINK)):
        link = ProductPageLocators.LINK[counter]
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page(counter)
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
