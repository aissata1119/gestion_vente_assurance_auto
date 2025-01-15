from django.db import models

# Create your models here.
class SubscriptionModel(models.Model):
    user_id = models.ForeignKey("user.UserModel", verbose_name="user_subscription", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    vehicle_info = models.JSONField("VehicleInfo",default="", null=True)
    subscriber_info = models.JSONField("SubscriberInfo",default="", null=True)