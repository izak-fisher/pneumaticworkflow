# Generated by Django 2.2.17 on 2021-03-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0106_connect_template_entities_with_wf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldselection',
            name='template',
        ),
        migrations.RemoveField(
            model_name='kickoffvalue',
            name='template',
        ),
        migrations.RemoveField(
            model_name='task',
            name='template',
        ),
        migrations.RemoveField(
            model_name='taskfield',
            name='template',
        ),
        migrations.AddField(
            model_name='fieldselection',
            name='template_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='kickoffvalue',
            name='template_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='template_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='taskfield',
            name='template_id',
            field=models.IntegerField(null=True),
        ),
    ]