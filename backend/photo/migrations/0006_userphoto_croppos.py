# Generated by Django 2.2.4 on 2019-09-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_userphoto_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='croppos',
            field=models.CharField(default='', max_length=250),
        ),
    ]
