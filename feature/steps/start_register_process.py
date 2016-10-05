from common import Wait_visibility_plink_text, Wait_visibility_tag, Wait_visibility_name
from behave import given, when, then


@given('the website "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    
@when('I click on the register button')
def step_impl(context):
    button_reg = Wait_visibility_plink_text(context, 'Зарегистрироваться')
    button_reg.click()

@then('I see the account register page')
def step_impl(context):
    assert 'Tickets Cloud' in context.driver.title
    assert 'Регистрация' in Wait_visibility_tag(context,'h1').text
    assert Wait_visibility_name(context, 'regForm')