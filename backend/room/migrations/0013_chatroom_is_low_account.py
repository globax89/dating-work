# Generated by Django 2.2.4 on 2019-09-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0012_auto_20190925_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_low_account',
            field=models.BooleanField(default=False, verbose_name='Is low account?'),
        ),
    ]
