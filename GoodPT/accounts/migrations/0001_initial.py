# Generated by Django 5.0 on 2023-12-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="USER",
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
                ("uuid", models.IntegerField(max_length=10)),
                ("body", models.TextField()),
                ("test", models.TextField()),
            ],
        ),
    ]
