from behave import given, when, then
from common import set_register_data, input_register_data, wait_visibility_class


@given('data of already registred user')
def step_impl(context):
    set_register_data(
        context=context,
        name='Vlad',
        mobile='+79189145456',
        email='abc_cba07@mail.ru',
        password='bddtest01')


@when('I enter data in regisration form')
def step_impl(context):
    input_register_data(context)


@when('select "{text}" in user group')
def step_impl(context, text):
    context.driver.find_element_by_id(text).click()


@when('click on the submit button')
def step_imp(context):
    button = context.driver.find_element_by_id('submit')
    button.click()


@then('I see warning with text "{warn}"')
def step_impl(context, warn):
    print(wait_visibility_class(context, 'ngn-message').text)
    assert warn in wait_visibility_class(context, 'ngn-message').text
