from behave import given
from common import wait_visibility_tag


@given('the page of company profile filling')
def step_impl(context):
    assert 'Создание профиля компании' in wait_visibility_tag(context, 'h1').text
