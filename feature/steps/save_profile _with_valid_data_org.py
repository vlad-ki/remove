from behave import given
from common import set_data_for_form, fake_ru, fake_en


@given('valid company data')
def step_impl(context):
    set_data_for_form(
        context=context,
        title=fake_ru.company(),
        cc_name=fake_ru.name(),
        cc_position=fake_ru.job(),
        cc_email=fake_en.email(),
        cc_phone=fake_ru.phone_number()
    )
