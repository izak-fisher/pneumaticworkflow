# Generated by Django 2.2.16 on 2020-11-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_auto_20201123_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(max_length=32),
        ),
    ]