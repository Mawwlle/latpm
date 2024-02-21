from rest_framework import serializers

from benchmark.models import Benchmark


class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = "__all__"
