# Generated by Django 4.2.5 on 2023-09-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("post_id", models.IntegerField(unique=True)),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("publish_date", models.DateTimeField()),
            ],
        ),
    ]
