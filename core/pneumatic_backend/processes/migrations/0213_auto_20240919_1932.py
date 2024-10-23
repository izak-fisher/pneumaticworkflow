# Generated by Django 2.2 on 2024-09-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0212_auto_20240919_1932'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rawperformertemplate',
            constraint=models.UniqueConstraint(
                condition=models.Q(is_deleted=False),
                fields=('template', 'api_name'),
                name='processes_rawperformertemplate_template_api_name_unique'
            ),
        )
    ]