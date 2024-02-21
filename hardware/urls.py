from django.urls import include, path
from rest_framework import routers

from hardware.views import ComputerViewSet, CPUInfoRetrieveView, CPUInfoViewSet

router = routers.SimpleRouter()
router.register(r"computers", ComputerViewSet)
router.register(r"cpus", CPUInfoViewSet)

urlpatterns = [
    path(
        r"cpus/<str:name>/", CPUInfoRetrieveView.as_view()
    ),  # because lookup_value_converter doesn't work
    path("", include(router.urls)),
]
