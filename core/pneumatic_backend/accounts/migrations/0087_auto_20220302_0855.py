# Generated by Django 2.2.26 on 2022-03-02 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0086_auto_20211216_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_newsletters_subscriber',
            field=models.BooleanField(default=True, help_text='customer.io emails'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_special_offers_subscriber',
            field=models.BooleanField(default=True, help_text='intercom emails'),
        ),
        migrations.CreateModel(
            name='UserCheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_created', models.BooleanField(default=False)),
                ('invite_team', models.BooleanField(default=False)),
                ('workflow_started', models.BooleanField(default=False)),
                ('template_owner_changed', models.BooleanField(default=False)),
                ('condition_created', models.BooleanField(default=False)),
                ('template_publicated', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='checklist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunSQL(
            """ INSERT INTO accounts_userchecklist (
                    template_created,
                    invite_team,
                    workflow_started,
                    template_owner_changed,
                    condition_created,
                    template_publicated,
                    user_id
                )
                    SELECT 
                        FALSE,
                        FALSE,
                        FALSE,
                        FALSE,
                        FALSE,
                        FALSE,
                        id
                    FROM accounts_user
                    WHERE is_deleted is FALSE """
        )
    ]