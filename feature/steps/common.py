from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait
from faker import Factory


fake_ru = Factory.create('ru_RU')
fake_en = Factory.create('en_US')


# Заполнение и проверка форм при регистрации
def set_data_for_form(context, **kwargs):
    for id, value in kwargs.items():
        setattr(context, 'form_{}'.format(id), value)


def input_data_to_form(context):
    for attr, value in context.__dict__['_stack'][0].items():
        if attr.startswith('form_'):
            element = context.driver.find_element_by_id(attr[5:])
            element.clear()
            element.send_keys(value)


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


"""
def wait_url(context, url):
    return WebDriverWait(context.driver, 120).until(
        context.driver.current_url == url) #must be callable
"""


def wait_text_to_be_present_in_element(context, tag, text):
    return WebDriverWait(context.driver, 120).until(
        es.text_to_be_present_in_element((By.TAG_NAME, tag), text)
    )
