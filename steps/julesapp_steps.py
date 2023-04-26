from behave import *


@given('login: I am a user on jules app page 2')
def step_impl(context):
    context.julesapp_page.navigate_to_jules_app()


@when('login: I click on sign up 2')
def step_impl(context):
    context.julesapp_page.click_sign_up()


@when('login: I verify the sign up page url "{url}"')
def step_impl(context, url):
    context.base_page.method_verify_url(url)


@when('login: I click on login 2')
def step_impl(context):
    context.julesapp_page.click_login_button()


@then('login: I verify the login page url "{url}"')
def step_impl(context, url):
    context.base_page.method_verify_url(url)
