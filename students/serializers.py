from rest_framework import serializers
from .models import *


class studentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = "__all__"


class student_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = (
            "id",
            "name",
            "father_name",
            "mother_name",
            "guardian_name",
            "dob",
            "reg_no",
        )


class student_classSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ("name", "stu_class", "stu_sec", "stu_roll", "id")


class student_contactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ["name", "primary_number", "whatsapp_number", "mail"]


class student_addressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ["name", "address1"]

