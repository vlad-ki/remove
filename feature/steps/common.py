from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
from faker import Factory


fake_ru = Factory.create('ru_RU')
fake_en = Factory.create('en_US')


# Заполнение и проверка форм
def Set_register_data(context, name, mobile, email, password):
    context.name = name
    context.mobile = mobile
    context.email = email
    context.password = password

def Input_register_data(context):
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

def Assert_warning_in_reg_fealds_by_id(*args, context):
    for arg in args:
        element = context.driver.find_element_by_id(arg)
        assert 'ng-dirty' in element.get_attribute('class')
        assert 'ng-invalid' in element.get_attribute('class')

# Ожидания
def Wait_tobe_clickable_link(context, link):
    return WebDriverWait(context.driver, 120).until(
        ES.element_to_be_clickable((By.LINK_TEXT, link))
        )

def Wait_tobe_located_id(context, id):
    return WebDriverWait(context.driver, 120).until(
        ES.presence_of_element_located((By.ID, id))
        )

def Wait_title_contains(context, title):
    return WebDriverWait(context.driver, 120).until(
        ES.title_contains(title))

def Wait_visibility_tag(context, tag):
    return WebDriverWait(context.driver, 120).until(
        ES.visibility_of_element_located((By.TAG_NAME, tag))
        )

def Wait_visibility_plink_text(context, plink):
    return WebDriverWait(context.driver, 120).until(
        ES.visibility_of_element_located((By.PARTIAL_LINK_TEXT, plink))
        )

def Wait_visibility_name(context, name):
    return WebDriverWait(context.driver, 120).until(
        ES.visibility_of_element_located((By.NAME, name))
        )

def Wait_elem_located_xpath(context, xpath):
    WebDriverWait(context.driver, 120).until(
        ES.presence_of_element_located((By.XPATH, xpath))
        )

def Wait_tobe_located_name(context, name):
    return WebDriverWait(context.driver, 120).until(
        ES.presence_of_element_located((By.NAME, name))
        )

