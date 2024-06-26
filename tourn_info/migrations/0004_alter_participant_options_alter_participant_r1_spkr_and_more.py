# Generated by Django 4.2.5 on 2024-01-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourn_info', '0003_team_cg_team_co_team_og_team_oo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'permissions': (('set_r3_spkr', "can set round 3's speaker points"), ('set_r4_spkr', "can set round 4's speaker points"), ('set_r5_spkr', "can set round 5's speaker points"))},
        ),
        migrations.AlterField(
            model_name='participant',
            name='r1_spkr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='r2_spkr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='r3_spkr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='r4_spkr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='r5_spkr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='r1_pt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='r2_pt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='r3_pt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='r4_pt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='r5_pt',
            field=models.IntegerField(default=0),
        ),
    ]
