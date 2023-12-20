# Generated by Django 4.2.7 on 2023-12-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0003_rename_datetime_question_create_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="postId",
        ),
        migrations.AddField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=0,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.TextField(),
        ),
    ]
