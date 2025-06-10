from fcm_django.models import AbstractFCMDevice
from django.db import models
from django.conf import settings


class CustomFCMDevice(AbstractFCMDevice):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='fcm_devices'
    )
    app_version = models.CharField(max_length=20, blank=True, null=True)
    device_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "FCM Device"
        verbose_name_plural = "FCM Devices"
