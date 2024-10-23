# Generated by Django 2.2 on 2023-10-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.TextField(blank=True, max_length=500, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(choices=[('signin', 'Sign in'), ('signup', 'Sign up'), ('signup-by-invite', 'Sign up by invite'), ('reset-password', 'Reset password'), ('forgot-password', 'Forgot password')], max_length=50, unique=True),
        ),
    ]
