from behave import when, then
from common import assert_valid_re_expression


@when('I check the re expression in fields')
def step_imppl(context):
    fields = {row['id']: row['re'] for row in context.table}
    assert_valid_re_expression(context=context, **fields)


@then('it\'s OK')
def step_impl(context):
    pass
