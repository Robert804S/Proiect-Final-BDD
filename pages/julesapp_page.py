from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class JulesApp(BasePage):

    SIGN_UP_BUTTON = (By. LINK_TEXT, "Sign up.")
    LOGIN_BUTTON = (By. XPATH, "//span[normalize-space()='Log In.']")

    def navigate_to_jules_app(self):
        self.driver.get("https://jules.app/sign-in")

    def click_sign_up(self):
        self.driver.find_element(*self.SIGN_UP_BUTTON).click()

    # method_verify_url("https://jules.app/sign-up")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # method_verify_url("https://jules.app/sign-in")
