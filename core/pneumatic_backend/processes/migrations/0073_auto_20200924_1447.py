# Generated by Django 2.2.16 on 2020-09-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0072_fileattachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileattachment',
            name='url',
            field=models.URLField(),
            preserve_default=False,
        ),
    ]
