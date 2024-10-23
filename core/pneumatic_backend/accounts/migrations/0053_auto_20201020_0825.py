# Generated by Django 2.2.16 on 2020-10-20 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from pneumatic_backend.generics.mixins.models import SoftDeleteMixin


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_auto_20200911_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('key', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(SoftDeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='user',
            name='is_robot',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='APILogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('path', models.CharField(max_length=1024)),
                ('method', models.CharField(max_length=8)),
                ('code', models.IntegerField(default=200)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='accounts.APIKey')),
            ],
            options={
                'ordering': ['-datetime'],
            },
            bases=(SoftDeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='apikey',
            name='robot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='apikey', to=settings.AUTH_USER_MODEL),
        ),
    ]
