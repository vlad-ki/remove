from behave import given, when
from common import set_data_for_form, input_data_to_form, fake_en, fake_ru


@given('invalid company data')
def step_impl(context):
    set_data_for_form(
        context=context,
        title=' ',
        cc_name=' ',
        cc_position=' ',
        cc_email=fake_en.email()[:-4],
        cc_phone=fake_ru.phone_number()[:9]
    )


@when('I enter data in the fields')
def step_impl(context):
    input_data_to_form(context)
    context.elements = ['title', 'cc_name', 'cc_position', 'cc_email', 'cc_phone']
    # нужно для проверки I see warnings
