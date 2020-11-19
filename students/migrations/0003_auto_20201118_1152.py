# Generated by Django 3.1.3 on 2020-11-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_due_session_yr'),
    ]

    operations = [
        migrations.AddField(
            model_name='due',
            name='deposit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='due',
            name='april',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='august',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='december',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='february',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='january',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='july',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='june',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='march',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='may',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='november',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='october',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='due',
            name='september',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
