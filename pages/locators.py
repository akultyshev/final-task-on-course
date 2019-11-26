from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_PRICE = (By.CLASS_NAME, "basket-mini")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_MESSAGES_DIV = (By.CSS_SELECTOR, "#messages .alertinner strong")
    SUCCESS_MESSAGES_DIV = (By.CSS_SELECTOR, "#messages .alert-success")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".content p")
    BASKET_TEXT = (By.CSS_SELECTOR, ".content h2")
