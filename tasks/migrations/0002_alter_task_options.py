# Generated by Django 5.1.6 on 2025-04-21 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "task",
                "verbose_name_plural": "tasks",
            },
        ),
    ]
