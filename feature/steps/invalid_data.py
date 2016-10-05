from common import Set_register_data, Input_register_data, fake_ru, fake_en
from common import Assert_warning_in_reg_fealds_by_id
from behave import given, when, then


@given('invalid data')
def step_impl(context):
    Set_register_data(context=context,
                        name=' ',
                        mobile=fake_ru.phone_number()[:9],
                        email=fake_en.email()[:-4],
                        password=fake_en.password(5))

@when('I enter invalid data')
def step_impl(context):
    Input_register_data(context)

@then('I see warning')
def step_impl(context):
    Assert_warning_in_reg_fealds_by_id('name', 'mobile', 'email', 'password', context=context)

@then('registration button is disabled')
def step_impl(context):
    button = context.driver.find_element_by_id("submit")
    assert not button.is_enabled()
