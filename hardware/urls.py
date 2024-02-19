from django.urls import include, path
from rest_framework import routers

from hardware.views import ComputerViewSet

router = routers.DefaultRouter()
router.register(r"computers", ComputerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]