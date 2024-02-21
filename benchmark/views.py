from rest_framework import mixins, viewsets

from benchmark.models import Benchmark
from benchmark.serializers import BenchmarkSerializer


class BenchmarkViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = BenchmarkSerializer
    queryset = Benchmark.objects.all()
