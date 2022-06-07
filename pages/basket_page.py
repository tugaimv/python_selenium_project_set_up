from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Cart doesn't empty"

    def should_be_message_that_basket_empty(self):
        basket_empty_txt = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TXT).text
        assert "Your basket is empty" in basket_empty_txt, "Basket doesn't contains message 'Your basket is empty'"
