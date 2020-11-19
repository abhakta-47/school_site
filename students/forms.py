from django.forms import ModelForm
from . import models


class student_detailsForm(ModelForm):
    class Meta:
        model = models.student
        fields = "__all__"


class studen_dueForm(ModelForm):
    class Meta:
        models = models.due
        fields = "__all__"

