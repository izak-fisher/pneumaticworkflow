# Generated by Django 2.2.26 on 2023-02-08 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0095_auto_20230208_1529'),
    ]

    operations = [
        migrations.RunSQL("""
            WITH accounts AS (
              SELECT
                aa.id,
                COUNT(au.id) AS active_users
              FROM accounts_user au
                INNER JOIN accounts_account aa
                  ON au.account_id = aa.id
              WHERE au.status = 'active'
                AND au.type = 'user'
                AND au.is_deleted IS FALSE
                AND aa.is_deleted IS FALSE
              GROUP BY aa.id
            )
            UPDATE accounts_account SET active_users=accounts.active_users
            FROM accounts
            WHERE accounts_account.id=accounts.id
        """),
        migrations.RunSQL("""
            WITH tenant AS (
              SELECT
                master_account_id AS id,
                SUM(tenant.active_users) AS tenants_active_users
              FROM accounts_account tenant
              WHERE tenant.lease_level = 'tenant'
                AND tenant.is_deleted IS FALSE
                AND master_account_id IS NOT NULL
              GROUP BY master_account_id
            )
            
            UPDATE accounts_account 
              SET active_users = accounts_account.active_users + 
                  tenant.tenants_active_users
            FROM tenant
            WHERE accounts_account.id=tenant.id
        """),
    ]
