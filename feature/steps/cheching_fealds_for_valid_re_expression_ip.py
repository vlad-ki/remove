from behave import when, then
from common import assert_valid_re_expression


@when('I check the re expression in fields')
def step_imppl(context):
    fields = {
        'ogrnip': '/^\d{15}$/',
        'inn': '/^\d{12}$/',
        'bik': '/^\d{9}$/',
        'ks': '/^\d{20}$/',
        'rs': '/^\d{20}$/'
    }
    assert_valid_re_expression(context=context, **fields)


@then('it\'s OK')
def step_impl(context):
    pass
