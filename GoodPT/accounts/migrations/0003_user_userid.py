# Generated by Django 4.2 on 2023-12-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0002_remove_user_body_remove_user_test_remove_user_uuid_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="userid",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
