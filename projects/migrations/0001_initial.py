# Generated by Django 4.1.3 on 2022-11-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=500)),
                ("technology", models.CharField(max_length=200)),
                ("cratedAt", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
