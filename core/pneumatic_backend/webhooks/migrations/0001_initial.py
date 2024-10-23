# Generated by Django 2.2.14 on 2020-08-04 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0045_auto_20200730_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.CharField(db_index=True, max_length=64, verbose_name='Event')),
                ('target', models.URLField(max_length=255, verbose_name='Target URL')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webhooks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
