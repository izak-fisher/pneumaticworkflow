# Generated by Django 2.2.7 on 2019-11-06 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applications',
            new_name='Application',
        ),
    ]