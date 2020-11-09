from django.db import models

# Create your models here.


class notices(models.Model):
    date = models.DateField()
    description = models.TextField()
    file = models.FileField()
