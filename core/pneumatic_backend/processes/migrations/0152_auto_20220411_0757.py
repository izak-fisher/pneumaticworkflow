# Generated by Django 2.2.27 on 2022-04-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0151_template_tasks_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
