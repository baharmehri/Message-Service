from django.urls import path, include

urlpatterns = [
    path('users/', include(('apps.users.urls', 'users'))),
    path('devices/', include(('apps.fcm_manager.urls', 'device-manager')), ),
]
