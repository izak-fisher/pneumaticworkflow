# Generated by Django 2.2.16 on 2020-09-21 11:36

from django.db import migrations


def fill_search_content(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0068_taskworkflow_search_content'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
            CREATE TRIGGER taskworkflow_ins BEFORE INSERT OR UPDATE ON processes_taskworkflow FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(search_content, 'pg_catalog.english', name, description);
            ''',
            reverse_sql='''
            DROP TRIGGER IF EXISTS taskworkflow_ins ON processes_taskworkflow;
            '''
        ),
        migrations.RunSQL(
            sql='''
            CREATE INDEX taskworkflow_idx ON processes_taskworkflow USING gin(search_content) WHERE is_deleted is FALSE;
            ''',
            reverse_sql='''
            DROP INDEX IF EXISTS taskworkflow_idx;
            '''
        ),
        migrations.RunPython(fill_search_content, reverse_code=migrations.RunPython.noop),
    ]
