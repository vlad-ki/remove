from behave import given, when, then
from common import (fake_ru, fake_en, set_data_for_form, input_data_to_form, wait_visibility_id,
                    wait_visibility_tag, wait_text_to_be_present_in_element)


@given('valid requisites data')
def step_impl(context):
    set_data_for_form(
        context=context,
        addr=fake_ru.address(),
        ogrnip=fake_en.random_number(15),
        inn=fake_en.random_number(12),
        bank_name=fake_en.company(),
        bik=fake_en.random_number(9),
        ks=fake_en.random_number(20),
        rs=fake_en.random_number(20)
    )


@when('I enter valid requisites data in the field')
def step_impl(context):
    fio = context.driver.find_element_by_xpath(
        '//input[@ng-model="legalEdit.legal.detail.name"]')  # нет id у fio
    fio.clear()
    fio.send_keys(fake_ru.name())

    input_data_to_form(context)


@when('check NDS with sistem of taxation')
def step_impl(context):
    elem_pay = context.driver.find_element_by_xpath(
        '//div[@ng-model="legalEdit.legal.detail.$nds"]')  # тут тоже нет id
    elem_pay.click()
    wait_visibility_id(context, 'ui-select-choices-row-0-0').click()

    elem_pay.click()
    wait_visibility_id(context, 'ui-select-choices-row-0-1').click()

    elem_tax = context.driver.find_element_by_xpath(
        '//div[@ng-model="legalEdit.legal.detail.taxes"]')  # и здесь нет id
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
    wait_text_to_be_present_in_element(context, 'h1', text)
