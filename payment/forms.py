from django.forms import ModelForm
from . import models


class priceModels(ModelForm):
    class Meta:
        model = models.price
        fields = "__all__"

