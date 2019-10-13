# Generated by Django 2.2.4 on 2019-09-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_agency2woman'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency2woman',
            options={'verbose_name': 'Agency woman', 'verbose_name_plural': 'Agency women'},
        ),
        migrations.AlterModelOptions(
            name='agencyfiles',
            options={'verbose_name': 'Agency file', 'verbose_name_plural': 'Agency files'},
        ),
        migrations.AlterField(
            model_name='agency',
            name='city',
            field=models.CharField(max_length=250, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='contact_email',
            field=models.CharField(max_length=250, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='director',
            field=models.CharField(max_length=250, verbose_name='Name and Surname of the Boss'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='login',
            field=models.CharField(help_text='Login', max_length=250, verbose_name='Login'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(help_text='Name', max_length=250, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='other_messanger',
            field=models.CharField(default='', help_text='Skype, telegram etc...', max_length=250, verbose_name='Other messangers'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='phone1',
            field=models.CharField(default='', max_length=250, verbose_name='Phone 1'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='phone2',
            field=models.CharField(default='', max_length=250, verbose_name='Phone 2'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='skype',
            field=models.CharField(default='', max_length=250, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='term',
            field=models.CharField(max_length=250, verbose_name='Term of work'),
        ),
    ]