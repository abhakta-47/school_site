# Generated by Django 3.1.3 on 2020-11-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20201118_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='april',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='august',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='december',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='february',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='january',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='july',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='june',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='march',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='may',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='november',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='october',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='september',
            field=models.CharField(default='due', max_length=20),
        ),
        migrations.AlterField(
            model_name='due',
            name='session',
            field=models.CharField(default='due', max_length=20),
        ),
    ]