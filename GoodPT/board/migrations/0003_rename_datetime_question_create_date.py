# Generated by Django 4.2.7 on 2023-12-20 05:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_answer_question_delete_board_answer_question"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="datetime",
            new_name="create_date",
        ),
    ]
