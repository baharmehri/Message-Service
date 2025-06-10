from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FCMDeviceViewSet

router = DefaultRouter()
router.register(r'', FCMDeviceViewSet, basename='fcm-device')

urlpatterns = [
    path('', include(router.urls)),
]
