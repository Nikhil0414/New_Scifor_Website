# Generated by Django 5.0.6 on 2024-06-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrer", "0015_delete_achievement_delete_employee_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casestudy",
            name="short_description",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
