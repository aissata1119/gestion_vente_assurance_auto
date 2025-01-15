from django.db import models

# Create your models here.
class VehicleCategoryModel(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)