# Generated by Django 2.2.28 on 2022-09-19 15:18
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0164_create_template_integrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='templateintegrations',
            name='shared_date',
            field=models.DateTimeField(null=True),
        )
    ]
