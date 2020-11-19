from django.db import models

# Create your models here.


class notice(models.Model):
    date = models.DateField()
    description = models.TextField()
    file = models.FileField()

    def __str__(self):
        return self.description
