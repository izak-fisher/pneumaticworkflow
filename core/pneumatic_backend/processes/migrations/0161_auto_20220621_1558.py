# Generated by Django 2.2.28 on 2022-06-21 15:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processes', '0160_taskperformer_date_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='run_allowed',
            new_name='template_owners',
        ),
        migrations.RunSQL(
            """ WITH with_t_owners_draft AS (
                  SELECT
                    id, 
                    jsonb_build_object('template_owners', draft->'run_allowed') AS draft
                  FROM processes_templatedraft
                  WHERE 
                    draft->'run_allowed' IS NOT NULL
                    AND is_deleted IS FALSE
                    AND (
                      draft->'template_owners' IS NULL
                      OR jsonb_array_length(draft->'template_owners') = 0
                    )
                )
                UPDATE processes_templatedraft ptd SET draft = ptd.draft || with_t_owners_draft.draft
                FROM with_t_owners_draft
                WHERE ptd.id = with_t_owners_draft.id """
        )
    ]
