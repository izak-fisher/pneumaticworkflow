# Generated by Django 2.2.17 on 2021-05-12 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0127_auto_20210511_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemtemplate',
            old_name='workflow_template',
            new_name='template',
        ),
    ]