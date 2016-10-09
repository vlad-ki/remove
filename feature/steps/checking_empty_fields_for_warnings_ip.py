from behave import given, when, then
from common import assert_warning_in_fealds_by_id, wait_visibility_tag, assert_empty_element_id


@given('the page of requisites filling')
def step_impl(context):
    assert 'Заполните реквизиты' in wait_visibility_tag(context, 'h1').text


@when('check that the felds are empty')
def step_impl(context):
    context.elements = ('addr', 'ogrnip', 'inn', 'bank_name', 'bik', 'ks', 'rs')
    assert_empty_element_id(*context.elements, context=context)


@when('the "{id}" is\'t check')
def step_impl(context, id):
    assert_empty_element_id(id, context=context)


@when('I click on the submit button')
def step_impl(context):
    elem_rs = context.driver.find_element_by_id('rs')
    elem_rs.submit()


@then('I see warnings')
def step_impl(context):
    assert_warning_in_fealds_by_id(*context.elements, context=context)
