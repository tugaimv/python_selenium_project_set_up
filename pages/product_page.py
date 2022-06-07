from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()

    def should_be_alert_that_the_product_has_been_added_to_the_basket(self):
        self.should_be_alert_block()
        self.should_be_product_name_in_alert()

    def should_be_alert_block(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED), "Product added alert is not presented"

    def should_be_product_name_in_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_txt = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_ADDED_INNER_TXT).text
        assert product_name == alert_txt, "Alert message don't contains product name"

    def should_be_alert_with_basket_cost(self):
        self.should_be_alert_price_block()
        self.should_be_price_in_alert()

    def should_be_alert_price_block(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_PRICE), "Cart price alert is not presented"

    def should_be_price_in_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_txt = self.browser.find_element(*ProductPageLocators.ALERT_CART_PRICE_TXT).text
        assert product_price == alert_txt, "Alert message don't contains product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_ADDED), "Success message is presented, " \
                                                                                      "but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappear(*ProductPageLocators.ALERT_PRODUCT_ADDED), "Success message doesn't disappear"
