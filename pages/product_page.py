from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_elt = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_elt.click()

    def should_be_basket_price_text(self):
        basket_price_elt = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        item_price_elt = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        assert item_price_elt.text in basket_price_elt.text, "Not verify item price in basket"

    def should_be_item_name(self):
        item_name_elt = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        messages_elt = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGES_DIV)
        assert item_name_elt.text == messages_elt.text, "Not verify item name in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES_DIV), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES_DIV), "Success message is presented, but should be disappeared"
