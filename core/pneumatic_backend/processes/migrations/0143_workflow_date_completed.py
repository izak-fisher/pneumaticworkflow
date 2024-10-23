# Generated by Django 2.2.24 on 2021-09-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0142_auto_20210810_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='date_completed',
            field=models.DateTimeField(null=True),
        ),
        migrations.RunSQL("""
        UPDATE processes_workflow pw 
        SET date_completed = pw.status_updated WHERE pw.status = 1
        """)
    ]
