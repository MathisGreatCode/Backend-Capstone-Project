# Generated by Django 4.1.7 on 2023-03-15 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_rename_table_menu"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Menu",
            new_name="MenuItem",
        ),
    ]