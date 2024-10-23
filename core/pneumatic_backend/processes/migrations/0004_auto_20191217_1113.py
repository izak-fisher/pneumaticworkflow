# Generated by Django 2.2.7 on 2019-12-17 11:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20191213_1037'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processes', '0003_process_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='Process',
            new_name='process',
        ),
        migrations.RemoveField(
            model_name='kickofffield',
            name='field_id',
        ),
        migrations.RemoveField(
            model_name='process',
            name='snapshot',
        ),
        migrations.RemoveField(
            model_name='processdef',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='step',
            name='step_id',
        ),
        migrations.RemoveField(
            model_name='stepfield',
            name='field_id',
        ),
        migrations.AddField(
            model_name='kickofffield',
            name='name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='kickofffield',
            name='type',
            field=models.PositiveIntegerField(choices=[(0, 'String'), (1, 'Text'), (2, 'Number'), (3, 'File')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='name',
            field=models.CharField(max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='process_def',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='processes.ProcessDef'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='steps_count',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='step',
            name='name',
            field=models.CharField(max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='number',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='step',
            name='responsible',
            field=models.ManyToManyField(related_name='step_responsible', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stepfield',
            name='type',
            field=models.PositiveIntegerField(choices=[(0, 'String'), (1, 'Text'), (2, 'Number'), (3, 'File')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='process',
            name='status',
            field=models.IntegerField(choices=[(0, 'Process in work'), (1, 'Process done')], default=0),
        ),
        migrations.AlterField(
            model_name='stepdef',
            name='responsible',
            field=models.ManyToManyField(related_name='def_responsible', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Snapshot',
        ),
    ]