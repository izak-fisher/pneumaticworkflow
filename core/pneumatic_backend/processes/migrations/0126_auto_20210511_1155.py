# Generated by Django 2.2.17 on 2021-05-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0125_auto_20210511_0636'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkflowDraft',
            new_name='TemplateDraft',
        )
    ]
