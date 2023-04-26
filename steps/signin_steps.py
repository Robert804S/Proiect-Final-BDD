from behave import *


@given('login: I am a user on the signin page')
def step_impl(context):
    context.signin_page.navigate_to_signin_page()


@when('login: I fill in an email "{email}"')
def step_impl(context, email):
    context.signin_page.input_email(email)


@when('login: I leave the password empty')
def step_impl(context):
    context.signin_page.leave_password_empty()


@when('login: I verify the error is displayed')
def step_impl(context):
    context.signin_page.verify_error()


@then('login: I check log in button is disabled')
def step_impl(context):
    context.signin_page.verify_login_button_is_disabled()
