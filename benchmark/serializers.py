from rest_framework import serializers

from benchmark.models import BenchmarkModel


class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkModel
        fields = "__all__"
