from behave import given, when, then
from common import (set_register_data, input_register_data, fake_ru, fake_en,
                    assert_warning_in_fealds_by_id)


@given('invalid registration data')
def step_impl(context):
    set_register_data(
        context=context,
        name=' ',
        mobile=fake_ru.phone_number()[:9],
        email=fake_en.email()[:-4],
        password=fake_en.password(5))


@when('I enter invalid data in registration form')
def step_impl(context):
    input_register_data(context)


@then('I see warning')
def step_impl(context):
    assert_warning_in_fealds_by_id('name', 'mobile', 'email', 'password', context=context)


@then('registration button is disabled')
def step_impl(context):
    button = context.driver.find_element_by_id("submit")
    assert not button.is_enabled()
