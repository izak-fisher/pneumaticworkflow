# Generated by Django 2.2.17 on 2021-06-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0135_auto_20210607_1145'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='conditiontemplate',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_conditiontemplate_template_api_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='fieldtemplate',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_fieldtemplate_template_api_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='fieldtemplateselection',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_fieldtemplateselection_template_api_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='predicatetemplate',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_predicatetemplate_template_api_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='ruletemplate',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('template', 'api_name'), name='processes_ruletemplate_template_api_name_unique'),
        ),
    ]
