# Generated by Django 3.1.3 on 2020-11-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_transaction_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trxn_no',
            field=models.CharField(max_length=20),
        ),
    ]