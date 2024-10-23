# Generated by Django 2.2 on 2023-07-17 17:43

from django.db import migrations, models
import django.db.models.deletion
import pneumatic_backend.generics.mixins.models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0187_auto_20230410_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemTemplateCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
                ('icon', models.URLField(max_length=1024, null=True)),
                ('color', models.CharField(help_text='color hex', max_length=20, null=True)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(pneumatic_backend.generics.mixins.models.SoftDeleteMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='systemtemplate',
            name='tasks_count',
        ),
        migrations.AlterField(
            model_name='systemtemplate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='systemtemplate',
            name='category',
            field=models.ForeignKey(
                help_text='for type "library"',
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='processes.SystemTemplateCategory'
            ),
        ),
    ]
