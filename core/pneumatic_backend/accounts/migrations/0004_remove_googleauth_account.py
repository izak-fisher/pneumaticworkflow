# Generated by Django 2.2.5 on 2019-10-03 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191003_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googleauth',
            name='account',
        ),
    ]