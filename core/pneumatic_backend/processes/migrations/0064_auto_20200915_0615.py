# Generated by Django 2.2.16 on 2020-09-15 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0063_taskfield_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kickoffvalue',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Process'),
        ),
        migrations.AddConstraint(
            model_name='kickoffvalue',
            constraint=models.UniqueConstraint(condition=models.Q(is_deleted=False), fields=('process',), name='kickoff_value_process_unique'),
        ),
    ]
