# Generated by Django 5.0.3 on 2024-04-02 19:03

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('custuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('aadhar', models.BigIntegerField()),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=50)),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('local_body', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.custuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='custuser',
            name='role',
            field=models.CharField(choices=[('Ward Member', 'Ward Member'), ('Users', 'Users')], default='Users', max_length=100),
        ),
    ]