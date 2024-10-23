# Generated by Django 2.2 on 2023-05-26 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pneumatic_backend.generics.mixins.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0004_auto_20230111_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_app',
            field=models.BooleanField(default=False, help_text='Indicates that the device is an Android or IOS application'),
        ),
        migrations.CreateModel(
            name='UserNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('count_unread_push_in_ios_app', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(pneumatic_backend.generics.mixins.models.SoftDeleteMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='usernotifications',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('user',), name='usernotifications_user_unique'),
        ),
        migrations.RunSQL("""
            UPDATE notifications_device SET is_app=TRUE
            FROM (
                SELECT id
                FROM notifications_device
                WHERE description LIKE 'Dart%'
            ) d
            WHERE 
                notifications_device.id = d.id
                AND is_deleted IS FALSE
        """),
        migrations.RunSQL("""
            INSERT INTO notifications_usernotifications (
                user_id,
                count_unread_push_in_ios_app,
                is_deleted
            ) SELECT
                user_id,
                0,
                FALSE
            FROM notifications_device
            WHERE
                description LIKE 'Dart%'
                AND is_deleted IS FALSE
            ON CONFLICT DO NOTHING
        """)
    ]
