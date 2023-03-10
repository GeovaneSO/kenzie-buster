# Generated by Django 4.1.4 on 2022-12-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="added_by",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "G"),
                    ("PG", "Pg"),
                    ("PG-13", "Pg 13"),
                    ("R", "R"),
                    ("NC-17", "Nc 17"),
                ],
                default="G",
                max_length=20,
            ),
        ),
    ]
