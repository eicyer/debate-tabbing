# Generated by Django 4.2.5 on 2024-02-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourn_info', '0005_lobby_outround_team_eliminated'),
    ]

    operations = [
        migrations.AddField(
            model_name='lobby',
            name='round',
            field=models.IntegerField(default=1),
        ),
    ]