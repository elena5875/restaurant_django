# Generated by Django 4.2.11 on 2024-06-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_review_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_posted',
            field=models.BooleanField(default=False),
        ),
    ]