# Generated by Django 4.2.11 on 2024-06-15 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_reservation_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
