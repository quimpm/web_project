from behave import *
use_step_matcher("parse")

@given(u'There are bands')
def step_impl(context):
    from apps.main.models import Band
    from django.contrib.auth import get_user_model
    User = get_user_model()
    for row in context.table:
        user = User.objects.create_user(
                username=row['user'], password=row['password']
                )
        Band(
                web_link=row['web_link'],
                playlist=row['playlist'],
                email=row['mail'],
                mobile=row['mobile'],
                user=user
                ).save()


@when(u'I list bands')
def step_impl(context):
    context.browser.visit(context.get_url('band_list'))


@then(u'I\'m viewing a list containing some of the bands')
def step_impl(context):
    mails = context.browser.find_by_name('list_mail')
    mobiles = context.browser.find_by_name('list_mobile')
    for i, row in enumerate(context.table):
        assert row['mail'] == mails[i].text
        assert row['mobile'] == mobiles[i].text

@then(u'The list contains {count:n} bands')
def step_impl(context, count):
    assert count == len(context.browser.find_by_name('list_mail'))
