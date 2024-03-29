# Generated by Django 4.2 on 2023-12-19 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="body",
        ),
        migrations.RemoveField(
            model_name="user",
            name="test",
        ),
        migrations.RemoveField(
            model_name="user",
            name="uuid",
        ),
        migrations.AddField(
            model_name="user",
            name="birthday",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
