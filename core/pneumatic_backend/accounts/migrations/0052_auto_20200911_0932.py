# Generated by Django 2.2.16 on 2020-09-11 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_user_search_content'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
            CREATE TRIGGER user_ins BEFORE INSERT OR UPDATE ON accounts_user FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(search_content, 'pg_catalog.english', first_name, last_name, email);
            ''',
            reverse_sql='''
            DROP TRIGGER IF EXISTS user_ins ON accounts_user;
            '''
        ),
        migrations.RunSQL(
            sql='''
            CREATE INDEX user_idx ON accounts_user USING gin(search_content) WHERE is_deleted is FALSE;
            ''',
            reverse_sql='''
            DROP INDEX IF EXISTS user_idx;
            '''
        ),
    ]
