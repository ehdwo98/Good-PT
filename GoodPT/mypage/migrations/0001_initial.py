# Generated by Django 4.2 on 2023-12-27 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("intro", models.TextField()),
                (
                    "useremail",
                    models.EmailField(max_length=128, verbose_name="사용자_이메일"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="사용자_전화번호"),
                ),
                ("address", models.CharField(max_length=50, verbose_name="사용자_주소")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="사용자",
                    ),
                ),
            ],
        ),
    ]
