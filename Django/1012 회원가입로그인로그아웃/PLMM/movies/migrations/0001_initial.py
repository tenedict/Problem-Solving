# Generated by Django 4.1.2 on 2022-10-13 04:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=20, null=True)),
                ("content", models.TextField()),
                ("movie_name", models.CharField(max_length=20, null=True)),
                (
                    "grade",
                    models.IntegerField(
                        help_text="0~5사이 값으로 입력하세요",
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("hits", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
