# Generated by Django 2.2.4 on 2019-09-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0004_auto_20190907_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='useronline',
            name='token',
            field=models.CharField(db_index=True, max_length=250, null=True),
        ),
    ]
