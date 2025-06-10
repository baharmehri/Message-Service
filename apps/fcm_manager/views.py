from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CustomFCMDevice
from .serializers import CustomFCMDeviceSerializer


class FCMDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = CustomFCMDeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomFCMDevice.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        registration_id = request.data.get('registration_id')
        device, created = CustomFCMDevice.objects.update_or_create(
            user=request.user,
            registration_id=registration_id,
            defaults={
                'app_version': request.data.get('app_version'),
                'device_name': request.data.get('device_name'),
            }
        )
        serializer = self.get_serializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
