# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *

#Регистрация уже имеющегося пользователя
@given('website "https://dev.ticketscloud.org" and click "Зарегистрироваться"')
def step(context):
    context.driver = webdriver.Firefox()
    context.driver.get('https://dev.ticketscloud.org')
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
    elem_email.send_keys('abc_cba08@mail.ru')

@then('page include text "Заполните реквизиты"')
def step(context):
    assert 'Заполните реквизиты' in context.driver.page_source
    context.driver.close()



