# Generated by Django 2.2.4 on 2019-09-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props', '0003_auto_20190918_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='alias',
            field=models.CharField(default='', help_text='Alias', max_length=250, verbose_name='Alias'),
            preserve_default=False,
        ),
    ]