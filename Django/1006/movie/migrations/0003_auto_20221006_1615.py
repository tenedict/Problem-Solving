# Generated by Django 3.2.13 on 2022-10-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20221006_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='active',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='summary',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
