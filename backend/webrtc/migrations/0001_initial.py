# Generated by Django 2.2.4 on 2019-09-13 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_userprofile_is_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Ice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ice', models.TextField(default='')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webrtc.Offer')),
            ],
        ),
    ]
