from behave import given, when, then
from common import (set_data_for_form, input_data_to_form, fake_ru, fake_en,
                    assert_warning_in_fealds_by_id)


@given('invalid registration data')
def step_impl(context):
    set_data_for_form(
        context=context,
        name=' ',
        mobile=fake_ru.phone_number()[:9],
        email=fake_en.email()[:-4],
        password=fake_en.password(5))


@when('I enter invalid data in registration form')
def step_impl(context):
    input_data_to_form(context)
    context.elements = ['name', 'mobile', 'email', 'password']
    # нужно для проверки I see warnings


@then('registration button is disabled')
def step_impl(context):
    button = context.driver.find_element_by_id("submit")
    assert not button.is_enabled()
