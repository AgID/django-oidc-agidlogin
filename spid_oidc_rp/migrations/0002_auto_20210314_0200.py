# Generated by Django 3.1.7 on 2021-03-14 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spid_oidc_rp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oidcauthenticationrequest',
            name='authz_url',
        ),
        migrations.RemoveField(
            model_name='oidcauthenticationrequest',
            name='code_challenge',
        ),
        migrations.RemoveField(
            model_name='oidcauthenticationrequest',
            name='code_challenge_method',
        ),
        migrations.RemoveField(
            model_name='oidcauthenticationrequest',
            name='code_verifier',
        ),
    ]
