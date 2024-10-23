# Generated by Django 2.2.17 on 2021-05-11 06:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0071_account_max_active_workflows'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processes', '0124_auto_20210507_0914'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                DROP TRIGGER iF EXISTS taskworkflow_ins
                ON processes_taskworkflow
            ''',
            reverse_sql='''
                CREATE TRIGGER taskworkflow_ins BEFORE INSERT OR UPDATE 
                ON processes_taskworkflow 
                    FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(
                        search_content,
                        'pg_catalog.english', 
                        name,
                        description
                    )'''
        ),
        migrations.RunSQL(
            sql='DROP INDEX IF EXISTS taskworkflow_idx',
            reverse_sql='''
                CREATE INDEX taskworkflow_idx 
                    ON processes_taskworkflow USING gin(search_content) 
                WHERE is_deleted is FALSE''',
        ),
        migrations.RemoveConstraint(
            model_name='taskworkflow',
            name='processes_taskworkflow_workflow_api_name_unique',
        ),
        migrations.RenameModel(
            old_name='TaskWorkflow',
            new_name='TaskTemplate',
        ),
        migrations.RunSQL(
            sql='''
            CREATE TRIGGER tasktemplate_ins BEFORE INSERT OR UPDATE 
            ON processes_tasktemplate 
                FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(
                    search_content,
                    'pg_catalog.english', 
                    name, 
                    description
            )''',
            reverse_sql='''
                DROP TRIGGER iF EXISTS tasktemplate_ins
                    ON processes_tasktemplate
            '''
        ),
        migrations.RunSQL(
            sql='''
                CREATE INDEX tasktemplate_idx 
                    ON processes_tasktemplate USING gin(search_content) 
                WHERE is_deleted is FALSE
            ''',
            reverse_sql='DROP INDEX IF EXISTS tasktemplate_idx'
        ),
        migrations.AddConstraint(
            model_name='tasktemplate',
            constraint=models.UniqueConstraint(
                condition=models.Q(is_deleted=False),
                fields=('workflow', 'api_name'),
                name='processes_tasktemplate_workflow_api_name_unique'),
        ),
    ]