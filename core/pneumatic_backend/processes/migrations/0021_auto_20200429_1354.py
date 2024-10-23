# Generated by Django 2.2.12 on 2020-04-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0020_auto_20200427_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='kickofffieldtemplate',
            name='api_name',
            field=models.CharField(max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kickofffieldtemplate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kickofffieldtemplate',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kickofffieldtemplate',
            name='type',
            field=models.PositiveIntegerField(choices=[(0, 'String'), (1, 'Text')]),
        ),
        migrations.AlterField(
            model_name='taskfield',
            name='type',
            field=models.PositiveIntegerField(choices=[(0, 'String'), (1, 'Text')]),
        ),
        migrations.AlterField(
            model_name='taskfieldtemplate',
            name='type',
            field=models.PositiveIntegerField(choices=[(0, 'String'), (1, 'Text')]),
        ),
        migrations.DeleteModel(
            name='KickoffField',
        ),
    ]