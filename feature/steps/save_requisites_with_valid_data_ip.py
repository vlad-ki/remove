from behave import given, when, then
from common import (fake_ru, fake_en, set_register_data_requisites,
                    input_register_data_requisites, wait_visibility_id,
                    wait_visibility_tag)


@given('valid requisites data')
def step_impl(context):
    set_register_data_requisites(
        context=context,
        fio=fake_ru.name(),
        address=fake_ru.address(),
        ogrn=fake_en.random_number(15),
        inn=fake_en.random_number(12),
        bank=fake_en.company(),
        bik=fake_en.random_number(9),
        ks=fake_en.random_number(20),
        rs=fake_en.random_number(20)
    )


@when('I enter valid requisites data in the field')
def step_impl(context):
    input_register_data_requisites(context)


@when('check NDS with sistem of taxation')
def step_impl(context):
    elem_pay = context.driver.find_element_by_xpath(
        '//div[@ng-model="legalEdit.legal.detail.$nds"]')
    elem_pay.click()
    wait_visibility_id(context, 'ui-select-choices-row-0-0').click()

    elem_pay.click()
    wait_visibility_id(context, 'ui-select-choices-row-0-1').click()

    elem_tax = context.driver.find_element_by_xpath(
        '//div[@ng-model="legalEdit.legal.detail.taxes"]')
    elem_tax.click()
    wait_visibility_id(context, 'ui-select-choices-row-1-0').click()

    elem_tax.click()
    wait_visibility_id(context, 'ui-select-choices-row-1-1').click()


@when('check "I agree with the EULA"')
def step_inpl(context):
    elem_license = context.driver.find_element_by_id('license_agreement')
    elem_license.click()


@then('I see "{text}"')
def step_impl(context, text):
    assert '/settings/partners/create' in context.driver.current_url
    assert text in wait_visibility_tag(context, 'h1').text
