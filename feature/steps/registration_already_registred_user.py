from behave import given, when, then
from common import set_data_for_form, input_data_to_form, wait_visibility_class


@given('data of already registred user')
def step_impl(context):
    set_data_for_form(
        context=context,
        name='Vlad',
        mobile='+79189145456',
        email='abc_cba07@mail.ru',
        password='bddtest01')


@when('I enter data in regisration form')
def step_impl(context):
    input_data_to_form(context)


@when('select "{text}" in user group')
def step_impl(context, text):
    context.driver.find_element_by_id(text).click()


@when('click on the submit button')
def step_imp(context):
    button = context.driver.find_element_by_id('submit')
    button.click()


@then('I see pop up window with text "{warn}"')
def step_impl(context, warn):
    assert warn in wait_visibility_class(context, 'ngn-message').text
