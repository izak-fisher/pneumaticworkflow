# Generated by Django 2.2 on 2024-06-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0118_auto_20240515_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='timezone',
            field=models.CharField(default='UTC', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'English (USA)'), ('es', 'Spanish'), ('de', 'German'), ('fr', 'French'), ('ru', 'Russian')], default='en', max_length=10),
        ),
    ]
