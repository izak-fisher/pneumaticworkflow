# Generated by Django 2.2.17 on 2020-12-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0099_merge_20201201_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name_template',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=280),
        ),
        migrations.AlterField(
            model_name='taskworkflow',
            name='name',
            field=models.CharField(max_length=280),
        ),
    ]
