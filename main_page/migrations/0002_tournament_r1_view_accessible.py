# Generated by Django 4.2.5 on 2024-01-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='r1_view_accessible',
            field=models.BooleanField(default=False),
        ),
    ]
