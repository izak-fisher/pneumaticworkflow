# Generated by Django 2.2.26 on 2022-11-23 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0092_auto_20221123_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
    ]
