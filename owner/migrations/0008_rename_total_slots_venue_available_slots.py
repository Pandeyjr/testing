# Generated by Django 5.0.6 on 2024-06-24 17:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0007_rename_available_slots_venue_total_slots"),
    ]

    operations = [
        migrations.RenameField(
            model_name="venue",
            old_name="total_slots",
            new_name="available_slots",
        ),
    ]
