from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class JulesApp2(Browser):
    SIGN_UP_BUTTON = (By.LINK_TEXT, "Sign up.")
    PERSONAL = (By.XPATH, "//input[@value='personal']")
    CONTINUE = (By.XPATH, "//span[normalize-space()='CONTINUE']")
    FIELD = (By.XPATH, "//input[@placeholder='Type your answer here...']")
    ERROR_NOTIFICATION = (By.TAG_NAME, "p")
    INPUT_EMAIL = (By.XPATH, "//input[@placeholder='Type your answer here...']")

    def navigate_to_jules_app(self):
        self.driver.get("https://jules.app/sign-in")
        sleep(1)

    def click_sign_up(self):
        self.driver.find_element(*self.SIGN_UP_BUTTON).click()
        sleep(1)

    def click_on_personal(self):
        self.driver.find_element(*self.PERSONAL).click()
        sleep(1)

    def click_on_continue(self):
        self.driver.find_element(*self.CONTINUE).click()
        sleep(1)

    def input_first_name(self, first_name):
        self.driver.find_element(*self.FIELD).send_keys(first_name)
        sleep(1)

    def enter_after_first_name(self):
        self.driver.find_element(*self.FIELD).send_keys(Keys.ENTER)
        sleep(1)

    def input_last_name(self, last_name):
        self.driver.find_element(*self.FIELD).send_keys(last_name)
        sleep(1)

    def enter_after_last_name(self):
        self.driver.find_element(*self.FIELD).send_keys(Keys.ENTER)
        sleep(1)

    def enter_wrong_email(self, wrong_email):
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(wrong_email)
        sleep(1)

    def verify_error(self):
        error = self.driver.find_element(*self.ERROR_NOTIFICATION)
        EC.text_to_be_present_in_element((By.TAG_NAME, "p"), 'Please enter a valid email address.')
        error.is_displayed()

        # actual = self.driver.find_element(*self.ERROR_NOTIFICATION).text
        # expected = "Please enter a valid email address."
        # assert expected in actual

    def clear_email_input(self):
        self.driver.find_element(*self.FIELD).send_keys(Keys.BACKSPACE * 12)


    def enter_correct_email(self, correct_email):
        self.driver.find_element(*self.FIELD).send_keys(correct_email)

    def verify_error_is_not_displayed_anymore(self):
        try:
            self.driver.find_element(*self.ERROR_NOTIFICATION)
        except Exception as e:
            # print(e)
            print("Eroarea a disparut")


# obiect = JulesApp2()
# obiect.navigate_to_jules_app()
# sleep(1)
# obiect.click_sign_up()
# sleep(1)
# obiect.click_on_personal()
# sleep(1)
# obiect.click_on_continue()
# sleep(1)
# obiect.input_first_name('Robert')
# sleep(1)
# obiect.enter_after_first_name()
# sleep(1)
# obiect.input_last_name('Stanescu')
# sleep(1)
# obiect.enter_after_last_name()
# sleep(1)
# obiect.enter_wrong_email('wrong_email')
# sleep(1)
# obiect.verify_error()
# sleep(1)
# obiect.clear_email_input()
# sleep(1)
# obiect.enter_correct_email('abc@gmail.com')
# sleep(1)
# obiect.verify_error_is_not_displayed_anymore()
