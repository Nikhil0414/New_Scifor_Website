# Generated by Django 5.0.6 on 2024-06-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrer", "0014_achievement"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Achievement",
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.AlterField(
            model_name="casestudy",
            name="short_description",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
