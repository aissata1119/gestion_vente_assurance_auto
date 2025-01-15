from django.db import models

# Create your models here.
class ProductModel(models.Model):
    subcription_id = models.ForeignKey("subscription.SubscriptionModel", verbose_name="subscription_product_id", on_delete=models.CASCADE)
    simulation_id = models.ForeignKey("simulation.SimulationModel", verbose_name="simulation_product_id", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField("vehicleCategory.VehicleCategoryModel", verbose_name="vehicleCategory_product_id")
    guarantees = models.ManyToManyField("garantee.GaranteeModel", verbose_name="garantee_product_id")