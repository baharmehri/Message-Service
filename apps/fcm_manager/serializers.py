from rest_framework import serializers
from .models import CustomFCMDevice


class CustomFCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFCMDevice
        fields = ['id', 'registration_id', 'app_version', 'device_name']
