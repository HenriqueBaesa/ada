# Generated by Django 4.1.7 on 2023-04-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professors", "0002_remove_professors_avatar_professors_is_staff_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professors",
            name="is_staff",
            field=models.BooleanField(default=True, verbose_name="staff status"),
        ),
    ]
