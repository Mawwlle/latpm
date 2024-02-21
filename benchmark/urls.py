from django.urls import include, path
from rest_framework import routers

from benchmark.views import BenchmarkViewSet

router = routers.DefaultRouter()
router.register(r"benchmarks", BenchmarkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
