# Generated by Django 2.2.4 on 2019-10-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_userprofile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
    ]
