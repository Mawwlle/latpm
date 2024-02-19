from rest_framework import viewsets, mixins
from benchmark.models import Benchmark

from benchmark.serializers import BenchmarkSerializer


class BenchmarkViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = BenchmarkSerializer
    queryset = Benchmark.objects.all()
