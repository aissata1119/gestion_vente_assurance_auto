from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.viewsets.garantee_viewsets import GaranteeViewSet
from api.viewsets.product_viewsets import ProductViewSet
from api.viewsets.simulation_viewsets import SimulationViewSet
from api.viewsets.subscription_viewsets import SubscriptionViewSet
from api.viewsets.user_viewsets import UserViewSet
from api.viewsets.vehicleCategory_viewsets import VehicleCategoryViewSet


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'Vehicle category',VehicleCategoryViewSet)
router.register(r'Subscription',SubscriptionViewSet)
router.register(r'Simulation',SimulationViewSet )
router.register(r'product',ProductViewSet)
router.register(r'Guarantee',GaranteeViewSet)
router.register(r'users',UserViewSet , basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]