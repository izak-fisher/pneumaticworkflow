# Generated by Django 2.2 on 2023-05-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0103_migrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='stripe_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]