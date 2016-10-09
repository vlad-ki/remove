from behave import given, when
from common import (fake_en, set_register_data_requisites,
                    input_register_data_requisites)


@given('invalid data')
def step_impl(context):
    set_register_data_requisites(
        context=context,
        fio=' ',
        address=' ',
        ogrn=fake_en.random_number(14),
        inn=fake_en.random_number(11),
        bank=' ',
        bik=fake_en.random_number(8),
        ks=fake_en.random_number(19),
        rs=fake_en.random_number(19)
    )


@when('I enter invalid data in the fields')
def step_impl(context):
    input_register_data_requisites(context=context)
    context.elements = ('addr', 'ogrnip', 'inn', 'bank_name', 'bik', 'ks', 'rs')
    # нужно для проверки I see warnings
