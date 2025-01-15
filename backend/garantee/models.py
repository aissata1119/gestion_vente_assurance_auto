from django.db import models

# Create your models here.
class GaranteeModel(models.Model):
    Type = models.CharField( max_length=255,blank=True, null=True, default="")
    rate = models.FloatField()
    min_premium = models.DecimalField(max_digits=5, decimal_places=2)