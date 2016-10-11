from behave import given, when
from common import fake_en, set_data_for_form, input_data_to_form


@given('invalid requisites data')
def step_impl(context):
    set_data_for_form(
        context=context,
        addr=' ',
        ogrnip=fake_en.random_number(14),
        inn=fake_en.random_number(11),
        bank_name=' ',
        bik=fake_en.random_number(8),
        ks=fake_en.random_number(19),
        rs=fake_en.random_number(19)
    )


@when('I enter invalid data in the fields')
def step_impl(context):
    fio = context.driver.find_element_by_xpath(
        '//input[@ng-model="legalEdit.legal.detail.name"]')  # нет id у fio
    fio.clear()
    fio.send_keys(' ')

    input_data_to_form(context=context)
    context.elements = ('addr', 'ogrnip', 'inn', 'bank_name', 'bik', 'ks', 'rs')
    # нужно для проверки I see warnings
