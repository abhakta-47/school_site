# Generated by Django 3.1.3 on 2020-11-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_transaction_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='details',
            field=models.JSONField(),
        ),
    ]