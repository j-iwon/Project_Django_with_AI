# Generated by Django 5.0.2 on 2024-05-17 14:48

import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("club", "0004_alter_club_club_info"),
        ("teenplay_server", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="clubpost",
            managers=[
                ("enabled_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="clubpostreply",
            managers=[
                ("enabled_objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="club",
            name="club_main_category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="teenplay_server.category",
            ),
        ),
        migrations.CreateModel(
            name="ClubCategory",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("status", models.BooleanField(default=1)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="teenplay_server.category",
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="club.club"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_club_category",
            },
        ),
    ]
