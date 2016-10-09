from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait
from faker import Factory


fake_ru = Factory.create('ru_RU')
fake_en = Factory.create('en_US')


# Заполнение и проверка форм при регистрации
def set_register_data(context, name, mobile, email, password):
    context.name = name
    context.mobile = mobile
    context.email = email
    context.password = password


def set_register_data_requisites(context, fio, address, ogrn, inn, bank, bik, ks, rs):
    context.fio = fio
    context.address = address
    context.ogrn = ogrn
    context.inn = inn
    context.bank = bank
    context.bik = bik
    context.ks = ks
    context.rs = rs


def input_register_data_requisites(context):
    fio = context.driver.find_element_by_xpath(
        '//input[@ng-model="legalEdit.legal.detail.name"]')
    fio.clear()
    fio.send_keys(context.fio)

    address = context.driver.find_element_by_id('addr')
    address.clear()
    address.send_keys(context.address)

    ogrn = context.driver.find_element_by_id('ogrnip')
    ogrn.clear()
    ogrn.send_keys(context.ogrn)

    inn = context.driver.find_element_by_id('inn')
    inn.clear()
    inn.send_keys(context.inn)

    bank = context.driver.find_element_by_id('bank_name')
    bank.clear()
    bank.send_keys(context.bank)

    bik = context.driver.find_element_by_id('bik')
    bik.clear()
    bik.send_keys(context.bik)

    ks = context.driver.find_element_by_id('ks')
    ks.clear()
    ks.send_keys(context.ks)

    rs = context.driver.find_element_by_id('rs')
    rs.clear()
    rs.send_keys(context.rs)


def input_register_data(context):
    name = context.driver.find_element_by_id('name')
    name.clear()
    name.send_keys(context.name)

    mobile = context.driver.find_element_by_id('mobile')
    mobile.clear()
    mobile.send_keys(context.mobile)

    email = context.driver.find_element_by_id('email')
    email.clear()
    email.send_keys(context.email)

    password = context.driver.find_element_by_id('password')
    password.clear()
    password.send_keys(context.password)


def assert_warning_in_fealds_by_id(*args, context):
    for arg in args:
        element = context.driver.find_element_by_id(arg)
        assert 'ng-dirty' in element.get_attribute('class')
        assert 'ng-invalid' in element.get_attribute('class')


def assert_empty_element_id(*args, context):
    for arg in args:
        element = context.driver.find_element_by_id(arg)
        assert ('ng-empty' in element.get_attribute('class') and
                'ng-dirty' not in element.get_attribute('class'))


def assert_valid_re_expression(context, **kwargs):
    try:
        for id, re in kwargs.items():
            element = context.driver.find_element_by_id(id)
            assert re in element.get_attribute('ng-pattern')
    except AssertionError:
        print('In field with id "{}" was changed re expression'.format(id))


# Ожидания
def wait_tobe_clickable_link(context, link):
    return WebDriverWait(context.driver, 120).until(
        es.element_to_be_clickable((By.LINK_TEXT, link))
    )


def wait_tobe_located_id(context, id):
    return WebDriverWait(context.driver, 120).until(
        es.presence_of_element_located((By.ID, id))
    )


def wait_title_contains(context, title):
    return WebDriverWait(context.driver, 120).until(
        es.title_contains(title))


def wait_visibility_tag(context, tag):
    return WebDriverWait(context.driver, 120).until(
        es.visibility_of_element_located((By.TAG_NAME, tag))
    )


def wait_visibility_plink_text(context, plink):
    return WebDriverWait(context.driver, 120).until(
        es.visibility_of_element_located((By.PARTIAL_LINK_TEXT, plink))
    )


def wait_visibility_name(context, name):
    return WebDriverWait(context.driver, 120).until(
        es.visibility_of_element_located((By.NAME, name))
    )


def wait_visibility_id(context, id):
    return WebDriverWait(context.driver, 120).until(
        es.visibility_of_element_located((By.ID, id))
    )


def wait_visibility_class(context, class_name):
    return WebDriverWait(context.driver, 120).until(
        es.visibility_of_element_located((By.CLASS_NAME, class_name))
    )


def wait_elem_located_xpath(context, xpath):
    WebDriverWait(context.driver, 120).until(
        es.presence_of_element_located((By.XPATH, xpath))
    )


def wait_tobe_located_name(context, name):
    return WebDriverWait(context.driver, 120).until(
        es.presence_of_element_located((By.NAME, name))
    )
