# Generated by Django 2.2.7 on 2019-11-08 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20191031_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.TextField(null=True, verbose_name='Company name'),
        ),
    ]
