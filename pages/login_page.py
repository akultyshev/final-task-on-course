from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_elt = self.browser.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email_elt.send_keys(email)
        password_elt = self.browser.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password_elt.send_keys(password)
        confirm_password_elt = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_TEXTBOX)
        confirm_password_elt.send_keys(password)
        register_button_elt = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button_elt.click()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
