# Generated by Django 5.0.3 on 2024-05-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='role',
            field=models.CharField(choices=[('WardMember', 'WardMember'), ('Users', 'Users')], default='Users', max_length=100),
        ),
    ]
