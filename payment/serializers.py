from payment.models import student

# , due_list, price_list, order
from rest_framework import serializers


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        exclude = ["date_of_birth"]
