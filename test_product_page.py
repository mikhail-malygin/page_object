from .pages.product_page import ProductPage


def test_guest_can_see_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders" \
           "-handbook_209/?promo=newYear "
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders" \
           "-handbook_209/?promo=newYear "
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()