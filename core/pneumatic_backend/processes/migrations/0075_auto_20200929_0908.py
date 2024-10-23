# Generated by Django 2.2.16 on 2020-09-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0074_merge_20200928_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileattachment',
            name='thumbnail_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='url',
            field=models.URLField(max_length=1024),
        ),
    ]