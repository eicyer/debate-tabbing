# Generated by Django 4.2.5 on 2024-04-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourn_info', '0009_adjudicator_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adjudicator',
            name='commitee',
        ),
        migrations.RemoveField(
            model_name='lobby',
            name='adjudicator',
        ),
        migrations.RemoveField(
            model_name='teamassignment',
            name='adjudicator',
        ),
        migrations.AddField(
            model_name='lobby',
            name='adjudicators',
            field=models.ManyToManyField(to='tourn_info.adjudicator'),
        ),
    ]
