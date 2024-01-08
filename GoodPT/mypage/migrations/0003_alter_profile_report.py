# Generated by Django 4.2.7 on 2024-01-08 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0005_remove_report_category_remove_report_char_count_and_more"),
        ("mypage", "0002_profile_report"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_report",
                to="report.report",
            ),
        ),
    ]
