from browser import Browser
from pages.signin_page import SigninPage
from pages.julesapp2_page import JulesApp2
from pages.julesapp_page import JulesApp
from pages.base_page import BasePage


def before_all(context):
    context.browser = Browser()
    context.signin_page = SigninPage()
    context.julesapp2_page = JulesApp2()
    context.julesapp_page = JulesApp()
    context.base_page = BasePage()


def after_all(context):
    context.browser.close()
