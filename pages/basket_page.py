from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        self.is_empty_basket()

    def is_empty_basket(self):
        b = self.have_text_basket_is_empty()
        c = not(self.have_text_grow_in_basket())
        assert b and c, "Basket is not empty"

    def is_not_empty_basket(self):
        b = self.have_text_basket_is_empty()
        c = self.have_text_grow_in_basket()
        assert b & c, "Basket is empty"

    def have_text_basket_is_empty(self):
        try:
            text_elt = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
            return "Your basket is empty" in text_elt.text
        except NoSuchElementException:
            return False

    def have_text_grow_in_basket(self):
        try:
            header_elt = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
            return "Items to buy now" in header_elt.text
        except NoSuchElementException:
            return False
