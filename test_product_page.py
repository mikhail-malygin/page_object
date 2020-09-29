import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators, LoginPageLocators, BasketPageLocators
from .pages.basket_page import BasketPage
from mimesis import Person
import passgenerator


@pytest.mark.parametrize("link, valid_substring_product_page_url, product_name, product_price",
                         [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK,
                          ProductPageLocators.PRODUCT_CODERS_AT_WORK])
def test_guest_can_see_product_page(browser, link, valid_substring_product_page_url, product_name, product_price):
    # Go to a product page.
    # Check necessary attributes of the product page: valid url product page, presence name and product price
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(valid_substring_product_page_url, product_name, product_price)


@pytest.mark.parametrize("link", [pytest.param(ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK[0],
                                               marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    # Actually we always see success message after adding product to basket. We marked this test case as "XFAIL"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        product_url = ProductPageLocators.PRODUCT_THE_CITY_AND_THE_STARS[0]
        self.product_page = ProductPage(browser, product_url)
        self.product_page.open()
        self.product_page.go_to_login_page()
        self.login_page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        person = Person()
        name_new_user = person.full_name()
        email_new_user = person.email(domains=[name_new_user.replace(' ', '').lower() + '.com'])
        password_new_user = passgenerator.generate(10)
        self.login_page.register_new_user(email_new_user, password_new_user)
        self.login_page.should_be_authorized_user()

    @pytest.mark.parametrize("link", [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK[0],
                                      ProductPageLocators.PRODUCT_CODERS_AT_WORK[0]])
    def test_user_cant_see_success_message(self, browser, link):
        # Authorized user don't see a success message about adding the product in the basket when
        # the user has just opened the product page
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.there_is_no_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link, valid_substring_product_page_url, product_name, product_price",
                             [ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK])
    def test_user_can_add_product_to_basket(self, browser, link, valid_substring_product_page_url, product_name,
                                            product_price):
        # Check to add a product to the basket by authorized user.
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.should_be_product_page(valid_substring_product_page_url, product_name, product_price)
        self.product_page.add_product_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize("link, valid_substring_product_page_url, product_name, product_price",
                         [ProductPageLocators.PRODUCT_CODERS_AT_WORK])
def test_guest_can_add_product_to_basket(browser, link, valid_substring_product_page_url, product_name,
                                         product_price):
    # Check to add a product to the basket by unauthorized user.
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page(valid_substring_product_page_url, product_name, product_price)
    product_page.add_product_to_basket()


@pytest.mark.parametrize("link", [pytest.param(ProductPageLocators.PRODUCT_THE_SHELLCODERS_HANDBOOK[0],
                                               marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # Actually we always see success message after adding product to basket. We marked this test case as "XFAIL"
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_THE_CITY_AND_THE_STARS[0]
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Check necessary attributes of the empty basket
    link = ProductPageLocators.PRODUCT_THE_CITY_AND_THE_STARS[0]
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_link = BasketPageLocators.BASKET_LINK
    basket_page = BasketPage(browser, basket_link)
    basket_page.basket_is_empty()
