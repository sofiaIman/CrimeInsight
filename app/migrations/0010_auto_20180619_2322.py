# -*- coding: utf-8 -*-
# Generated by Django 2.2.15 on 2021-07-03 1:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180521_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='sanfran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(choices=[('SUN', 'Sunday'), ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')], max_length=10)),
                ('Location', models.CharField(choices=[('BAY', 'BAYVIEW'), ('CEN', 'CENTRAL'), ('ING', 'INGLESIDE'), ('MIS', 'MISSION'), ('NRT', 'NORTHERN'), ('PRK', 'PARK'), ('RIC', 'RICHMOND'), ('SOU', 'SOUTHERN'), ('TAR', 'TARAVAL'), ('TEN', 'TENDERLOIN')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Rape_Cases_Reported',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_Above_50_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_Between_10to14_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_Between_14to18_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_Between_18to30_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_Between_30to50_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_Upto_10_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Victims_of_Rape_Total',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Above_50_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Total',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Upto_10_15_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Upto_10_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Upto_15_18_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Upto_18_30_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Victims_Upto_30_50_Yrs',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
