# Generated by Django 4.1.3 on 2022-11-27 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_rename_cratedat_project_crated_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="crated_at",
            new_name="created_at",
        ),
    ]