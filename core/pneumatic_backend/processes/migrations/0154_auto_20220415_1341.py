# Generated by Django 2.2.27 on 2022-04-15 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0153_taskfield_workflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfield',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='processes.Workflow'),
        ),
    ]
