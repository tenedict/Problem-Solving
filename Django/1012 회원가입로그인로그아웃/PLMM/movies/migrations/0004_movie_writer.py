# Generated by Django 4.1.2 on 2022-10-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movie_hits"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="writer",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
