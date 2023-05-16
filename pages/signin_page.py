from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class SigninPage(Browser):
    INPUT_EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@placeholder='Enter your password']")
    ERROR_NOTIFICATION = (By.TAG_NAME, "p")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='MuiButton-label']")

    def navigate_to_signin_page(self):
        self.driver.get("https://jules.app/sign-in")

    def input_email(self, email):
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)

    def leave_password_empty(self):
        password = self.driver.find_element(*self.INPUT_PASSWORD)
        password.send_keys("a")
        password.send_keys(Keys.BACKSPACE)

    def verify_error(self):
        error = self.driver.find_element(*self.ERROR_NOTIFICATION)
        ec.text_to_be_present_in_element((By.TAG_NAME, "p"), 'Please enter your password!')
        error.is_displayed()

    def verify_login_button_is_disabled(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        sleep(1)
        login_button.get_attribute("disabled")
        print(login_button.get_attribute("disabled"))
