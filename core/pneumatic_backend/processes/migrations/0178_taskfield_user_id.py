# Generated by Django 2.2.28 on 2023-01-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0177_auto_20230117_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskfield',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelOptions(
            name='fileattachment',
            options={'ordering': ('id',)},
        ),
        migrations.RunSQL("""
            UPDATE processes_taskfield
              SET value=result.value
            FROM (
              SELECT distinct(f.id), s.value
              FROM processes_taskfield f
                INNER JOIN processes_fieldselection s ON f.id = s.field_id
              WHERE f.type in ('dropdown', 'radio')
                AND f.is_deleted IS FALSE
                AND s.is_deleted IS FALSE
                AND s.is_selected IS TRUE
            ) AS result
            WHERE processes_taskfield.id=result.id
        """),
        migrations.RunSQL("""
            UPDATE processes_taskfield
              SET
                value=result.value,
                user_id=result.user_id
            FROM (
              SELECT 
                f.id,
                u.id AS user_id,
                u.first_name || ' ' || u.last_name AS value
              FROM processes_taskfield f
                INNER JOIN accounts_user u ON f.value::int = u.id
              WHERE f.type = 'user'
                AND f.is_deleted IS FALSE
                AND f.value != ''
            ) AS result
            WHERE processes_taskfield.id=result.id
        """),
        migrations.RunSQL("""
            UPDATE processes_taskfield
            SET value=result.value
            FROM (
              SELECT
                f.id,
                string_agg(file.url, ', ' ORDER BY file.id) AS value
              FROM processes_taskfield f
                INNER JOIN processes_fileattachment file ON file.output_id = f.id
              WHERE f.type = 'file'
                AND f.is_deleted IS FALSE
                AND file.is_deleted is FALSE
                AND file.output_id IS NOT NULL
             GROUP BY f.id
             ORDER BY f.id
            ) AS result
            WHERE processes_taskfield.id=result.id
        """),
        migrations.RunSQL("""
        UPDATE processes_taskfield
            SET value=result.value
            FROM (
              SELECT
                f.id,
                f.name,
                string_agg(s.value, ', ' ORDER BY s.id) AS value
              FROM processes_taskfield f
                INNER JOIN processes_fieldselection s ON s.field_id = f.id
              WHERE f.type = 'checkbox'
                AND f.is_deleted IS FALSE
                AND s.is_deleted is FALSE
                AND s.is_selected IS TRUE
             GROUP BY f.id
             ORDER BY f.id
            ) AS result
            WHERE processes_taskfield.id=result.id
        """)
    ]
