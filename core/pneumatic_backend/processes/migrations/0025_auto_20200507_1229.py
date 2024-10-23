# Generated by Django 2.2.12 on 2020-05-07 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_userinvite_invited_from'),
        ('processes', '0024_auto_20200506_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kickofffieldtemplate',
            name='account',
        ),
        migrations.AddField(
            model_name='kickofffieldtemplate',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Kickoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='kickofffieldtemplate',
            name='kickoff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Kickoff'),
            preserve_default=False,
        ),
    ]
