from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from RK2_app.views import report, OperatingSystemViewSet, ComputerViewSet

router = routers.DefaultRouter()
router.register(r'OperatingSystem', OperatingSystemViewSet)
router.register(r'Computer', ComputerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('report/', report),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
