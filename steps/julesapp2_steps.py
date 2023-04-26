from behave import *


@given('login: I am a user on jules app page 3')
def step_impl(context):
    context.julesapp2_page.navigate_to_jules_app()


@when('login: I click on sign up')
def step_impl(context):
    context.julesapp2_page.click_sign_up()


@when('login: I click on personal')
def step_impl(context):
    context.julesapp2_page.click_on_personal()


@when('login: I click on continue')
def step_impl(context):
    context.julesapp2_page.click_on_continue()


@when('login: I input first name "{Robert}"')
def step_impl(context, Robert):
    context.julesapp2_page.input_first_name(Robert)


@when('login: I press enter after first name input')
def step_impl(context):
    context.julesapp2_page.enter_after_first_name()


@when('login: I input last name "{Stanescu}"')
def step_impl(context, Stanescu):
    context.julesapp2_page.input_last_name(Stanescu)


@when('login: I press enter after last name input')
def step_impl(context):
    context.julesapp2_page.enter_after_last_name()


@when('login: I enter wrong email "{email}"')
def step_impl(context, email):
    context.julesapp2_page.enter_wrong_email(email)


@when('login: I verify the error')
def step_impl(context):
    context.julesapp2_page.verify_error()


@when('login: I clear wrong email input')
def step_impl(context):
    context.julesapp2_page.clear_email_input()


@when('login: I enter correct email "{email}"')
def step_impl(context, email):
    context.julesapp2_page.enter_correct_email(email)


@then('login: I verify that the error is not displayed anymore')
def step_impl(context):
    context.julesapp2_page.verify_error_is_not_displayed_anymore()