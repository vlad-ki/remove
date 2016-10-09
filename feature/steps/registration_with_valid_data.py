from behave import given, when, then
from common import (set_register_data, input_register_data, fake_ru,
                    fake_en, wait_visibility_tag, wait_visibility_class)


@given('valid registration data')
def step_impl(context):
    set_register_data(
        context=context,
        name=fake_ru.name(),
        mobile=fake_ru.phone_number(),
        email=fake_en.email(),
        password=fake_en.password(9))


@when('I enter valid data in the registratio form')
def step_impl(context):
    input_register_data(context)


@then('I see the page of Personal Aria')
def step_impl(context):
    assert 'Новый партнер' in wait_visibility_class(context, 'account-info__name').text
