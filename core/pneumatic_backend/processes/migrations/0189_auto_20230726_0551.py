# Generated by Django 2.2 on 2023-07-26 05:51

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0188_auto_20230717_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemtemplatecategory',
            options={
                'ordering': ('order',),
                'verbose_name_plural': 'system template categories'
            },
        ),
        migrations.AddField(
            model_name='systemtemplate',
            name='search_content',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.RunSQL("""
            CREATE TRIGGER systemtemplate_ins 
            BEFORE INSERT OR UPDATE ON processes_systemtemplate
            FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(
                search_content, 
                'pg_catalog.english', 
                name,
                description
            )
        """)
    ]