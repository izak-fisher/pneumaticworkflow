# Generated by Django 2.2.16 on 2020-10-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_auto_20201020_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]