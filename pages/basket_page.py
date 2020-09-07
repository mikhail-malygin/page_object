from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage, BasketPageLocators):
    def basket_is_empty(self):
        self.there_is_no_product_in_basket()
        self.message_your_basket_is_empty()

    def there_is_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_FORM), "The basket isn't empty"

    def message_your_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE_FORM), \
            "There is no message 'Your basket is empty'"
