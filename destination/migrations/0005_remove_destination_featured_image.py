# Generated by Django 5.1.5 on 2025-01-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "destination",
            "0004_destination_featured_image_alter_review_destination_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="destination",
            name="featured_image",
        ),
    ]
