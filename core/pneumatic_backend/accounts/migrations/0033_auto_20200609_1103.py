# Generated by Django 2.2.13 on 2020-06-09 11:03

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_account_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clearbituserinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinvite',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('email',), name='user_email_unique'),
        ),
        migrations.AddConstraint(
            model_name='userinvite',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('email',), name='user_invite_email_unique'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(
                error_messages={'unique': 'A user with that username already exists.'},
                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                max_length=150,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name='username',
            ),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(
                condition=models.Q(is_deleted=False),
                fields=('username',),
                name='user_username_unique',
            ),
        ),
    ]
