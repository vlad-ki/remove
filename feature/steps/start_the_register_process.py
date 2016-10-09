from behave import given, when, then
from common import wait_visibility_plink_text, wait_visibility_tag, wait_visibility_name


@given('the website "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@when('I click on the register button')
def step_impl(context):
    button_reg = wait_visibility_plink_text(context, 'Зарегистрироваться')
    button_reg.click()


@then('I see the account register page')
def step_impl(context):
    assert 'Tickets Cloud' in context.driver.title
    assert 'Регистрация' in wait_visibility_tag(context, 'h1').text
    assert wait_visibility_name(context, 'regForm')
