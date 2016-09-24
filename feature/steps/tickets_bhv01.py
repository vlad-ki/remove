# -*- coding: utf-8 -*-
import random
import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from behave import *

RAND = random.randint(1,999999)

#Регистрация уже имеющегося пользователя
@given('website "https://dev.ticketscloud.org" and click "Зарегистрироваться"')
def step(context):
    context.driver = webdriver.Firefox()
    context.driver.get('https://stage.ticketscloud.org/#/')
    button_reg = context.driver.find_element_by_xpath('//a[@href="#/register"]')
    button_reg.click()
    assert 'Tickets Cloud' in context.driver.title

@then('whrite in field name and assert button disabled')
def step(context):
    elem_name = context.driver.find_element_by_id('name')
    elem_name.send_keys('Vlad')
    assert context.driver.find_element_by_xpath('//input[@disabled="disabled"]')

@then('whrite in field mobile and assert button disabled')
def step(context):
    elem_phone = context.driver.find_element_by_id('mobile')
    elem_phone.send_keys('+79189145456')
    assert context.driver.find_element_by_xpath('//input[@disabled="disabled"]')

@then('whrite in field email invalid value and assert warning')
def step(context):
    elem_email = context.driver.find_element_by_id('email')
    elem_email.send_keys('abc_cba07')
    assert context.driver.find_element_by_class_name('ng-invalid-pattern')

@then('whrite in field email valid value and assert button disabled')
def step(context):
    elem_email = context.driver.find_element_by_id('email')
    elem_email.send_keys('@mail.ru')
    assert context.driver.find_element_by_xpath('//input[@disabled="disabled"]')

@then('write in feald password invalid value and assert warning')
def step(context):
    elem_pass = context.driver.find_element_by_id('password')
    elem_pass.send_keys('bddt')
    assert context.driver.find_element_by_class_name('ng-invalid-pattern')

@then('whrite in field valid password')
def step(context):
    elem_pass = context.driver.find_element_by_id('password')
    elem_pass.send_keys('est01')

@then('select "Я - Организатор"')
def step(context):
    elem_select = context.driver.find_element_by_xpath('//input[@id="i-am-org"]')
    elem_select.click()

@then('push button and wait to get page source')
def step(context):
    elem_subm = context.driver.find_element_by_id('submit')
    elem_subm.click()
    time.sleep(0.5)

@then('page include text "Пользователь abc_cba07@mail.ru уже существует"')
def step(context):
    assert 'Пользователь abc_cba07@mail.ru уже существует' in context.driver.page_source
    context.driver.close()

@then('whrite in field email new email')
def step(context):
    elem_email = context.driver.find_element_by_id('email')
    elem_email.clear()
    elem_email.send_keys('abc_cba' + str(RAND) + '@mail.ru')

# Заполнение реквизитов
@then('page include text "Заполните реквизиты"')
def step(context):
    assert 'Заполните реквизиты' in context.driver.page_source

@then('click button "Индивидуальный предприниматель" in Personal Area')
def step(context):
    elem_ip = context.driver.find_element_by_xpath('//div[@class="tc-form__row"]/button[1]')
    elem_ip.click()
    assert 'Адрес регистрации' in context.driver.page_source

@then ('write in field "ФИО ПОЛНОСТЬЮ" and assert filling important fields')
def step(context):
    elem_fio = context.driver.find_element_by_xpath(
                '//input[@ng-model="legalEdit.legal.detail.name"]')
    elem_fio.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_fio.send_keys('Иванов Иван Иванович')

@then ('write in field "АДРЕС РЕГИСТРАЦИИ" and assert filling important fields')
def step(context):
    elem_address = context.driver.find_element_by_xpath(
                    '//input[@ng-model="legalEdit.legal.detail.address"]')
    elem_address.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_address.send_keys('г. Москва ул. Пушкина')

@then ('write in field "ОГРНИП" and assert filling important fields')
def step(context):
    elem_ogrnip = context.driver.find_element_by_xpath(
                    '//input[@ng-model="legalEdit.legal.detail.ogrnip"]')
    elem_ogrnip.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_ogrnip.send_keys('121232324565456')

@then ('write in field "ИНН" and assert filling important fields')
def step(context):
    elem_inn = context.driver.find_element_by_xpath(
                '//input[@ng-model="legalEdit.legal.detail.inn"]')
    elem_inn.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_inn.send_keys('565489654878')

@then ('choose value of "ХОЧУ ПОЛУЧАТЬ ПЛАТЕЖИ"')
def step(context):
    elem_pay = context.driver.find_element_by_xpath(
                '//div[@ng-model="legalEdit.legal.detail.$nds"]').click()
    elem_nds = context.driver.find_element_by_id(
                'ui-select-choices-row-0-0').click()
    elem_pay = context.driver.find_element_by_xpath(
                '//div[@ng-model="legalEdit.legal.detail.$nds"]').click()
    elem_nonds = context.driver.find_element_by_id(
                'ui-select-choices-row-0-1').click()

@then ('choose value of "СИСТЕМА НАЛОГООБЛАЖЕНИЯ"')
def step(context):
    lem_tax = context.driver.find_element_by_xpath(
                '//div[@ng-model="legalEdit.legal.detail.taxes"]').click()
    elem_ob = context.driver.find_element_by_id(
                'ui-select-choices-row-1-0').click()
    elem_tax = context.driver.find_element_by_xpath(
                '//div[@ng-model="legalEdit.legal.detail.taxes"]').click()
    elem_upr = context.driver.find_element_by_id(
                'ui-select-choices-row-1-1').click()

@then ('write in field "НАЗВАНИЕ БАНКА" and assert filling important fields')
def step(context):
    elem_bank = context.driver.find_element_by_id('bank_name')
    elem_bank.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_bank.send_keys('Первый Межгалактический')

@then ('write in field "БИК" and assert filling important fields')
def step(context):
    elem_bik = context.driver.find_element_by_id('bik')
    elem_bik.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_bik.send_keys('254648978')

@then ('write in field "КОРР.СЧЕТ" and assert filling important fields')
def step(context):
    elem_ks = context.driver.find_element_by_id('ks')
    elem_ks.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_ks.send_keys('85456320000120045630')

@then('write in field "РАСЧЕТНЫЙ СЧЕТ" and assert filling important fields')
def step(context):
    elem_rs = context.driver.find_element_by_id('rs')
    elem_rs.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_rs.send_keys('10000155038017705620')
    elem_rs.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')

@then('click on "Согласен с Лицензионным договором"')
def step(context):
    elem_license = context.driver.find_element_by_id('license_agreement')
    elem_license.click()

@then('click submit')
def step(context):
    elem_rs = context.driver.find_element_by_id('rs')
    elem_rs.submit()
    time.sleep(1)

# Создание профиля
@then ('click button "Организатор" in Personal Area')
def step(context):
    elem_org = context.driver.find_element_by_xpath('//div[@class="tc-form__row"]/button[1]')
    elem_org.click()
    assert 'Эквайринг' in context.driver.page_source

@then ('write in field "НАЗВАНИЕ БРЕНДА"')
def step(context):
    elem_brend = context.driver.find_element_by_id('title')
    elem_brend.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_brend.send_keys('Йода и КО')

@then ('choose acquiring')
def step(context):
    elem_vendor = context.driver.find_element_by_id('acquiring_vendor').click()
    elem_cost = context.driver.find_element_by_id('acquiring_customer').click()

#контактное лицо
@then ('write in feald "ИМЯ"')
def step(context):
    elem_ccname = context.driver.find_element_by_id('cc_name')
    elem_ccname.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_ccname.send_keys('Владимир')

@then ('write in feald "ДОЛЖНОСТЬ" and fields validity checking')
def step(context):
    elem_ccpos = context.driver.find_element_by_id('cc_position')
    elem_ccpos.submit()
    assert context.driver.find_element_by_class_name('ng-invalid-required')
    elem_ccpos.send_keys('Джедай')
    try:
        assert not context.driver.find_element_by_class_name('ng-invalid-required')
    except exceptions.NoSuchElementException as err:
        pass

# Проверка полей на нахождение ошибок
@then ('checking field "EMAIL" for checking valid values')
def step(context):
    elem_email = context.driver.find_element_by_id('email')
    elem_email.clear()
    elem_email.send_keys('abc_cba'+str(RAND)+'@mail.')
    assert context.driver.find_element_by_class_name('ng-invalid-pattern')
    elem_email.send_keys('ru')
    try:
        assert not context.driver.find_element_by_class_name('ng-invalid-pattern')
    except exceptions.NoSuchElementException as err:
        pass

@then ('checking field "ТЕЛЕФОН" for checking valid values')
def step(context):
    elem_phone = context.driver.find_element_by_id('phone')
    elem_phone.clear()
    elem_phone.send_keys('+7918914')
    assert context.driver.find_element_by_class_name('ng-invalid-pattern')
    elem_phone.send_keys('5456')
    try:
        assert not context.driver.find_element_by_class_name('ng-invalid-pattern')
    except exceptions.NoSuchElementException as err:
        pass

@then ('checking field "CC_EMAIL" for checking valid values')
def step(context):
    elem_ccemail = context.driver.find_element_by_id('cc_email')
    elem_ccemail.clear()
    elem_ccemail.send_keys('abc_cba'+str(RAND)+'@mail.')
    assert context.driver.find_element_by_class_name('ng-invalid-pattern')
    elem_ccemail.send_keys('ru')
    try:
        assert not context.driver.find_element_by_class_name('ng-invalid-pattern')
    except exceptions.NoSuchElementException as err:
        pass

@then ('checking field "CC_ТЕЛЕФОН" for checking valid values and submit')
def step(context):
    elem_ccphone = context.driver.find_element_by_id('cc_phone')
    elem_ccphone.clear()
    elem_ccphone.send_keys('+7918914')
    assert context.driver.find_element_by_class_name('ng-invalid-pattern')
    elem_ccphone.send_keys('5456')
    try:
        assert not context.driver.find_element_by_class_name('ng-invalid-pattern')
    except exceptions.NoSuchElementException as err:
        pass
    elem_ccphone.submit()
    time.sleep(0.5)
    assert 'Все данные успешно сохранены.' in context.driver.page_source
    context.driver.close()