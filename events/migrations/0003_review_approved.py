# Generated by Django 4.2.7 on 2023-12-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_review_delete_reviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
