# Generated by Django 2.2.4 on 2019-09-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_appsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
