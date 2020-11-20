# Generated by Django 3.1.3 on 2020-11-20 11:55

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_remove_transaction_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='details',
            field=models.JSONField(default=payment.models.transaction.detail_default),
        ),
    ]