# Generated by Django 2.2.4 on 2019-09-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_merge_20190925_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='hight',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default='1999-01-01'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goal',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lookingfor',
            field=models.TextField(default=''),
        ),
    ]
