from django.db import models

# Create your models here.
class SimulationModel(models.Model):
    user_id = models.ForeignKey("user.UserModel", verbose_name="user_subscription", on_delete=models.CASCADE)
    quote_reference = models.CharField( max_length=255)
    end_date = models.DateTimeField( blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)