# Generated by Django 4.2 on 2023-12-19 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "accounts",
            "0002_remove_user_body_remove_user_test_remove_user_uuid_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("postId", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=400)),
                ("content", models.CharField(max_length=20000)),
                ("isComplete", models.BooleanField()),
                ("datetime", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
                    ),
                ),
            ],
        ),
    ]
