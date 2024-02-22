from rest_framework import serializers

from hardware.models import (ComputerModel, CPUInfoModel, CPUMonitoringModel,
                             GPUInfoModel)


class CPUInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUInfoModel
        fields = "__all__"
        read_only_fields = ["id"]


class CPUMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUMonitoringModel
        fields = "__all__"
        read_only_fields = ["id"]


class GPUInfoSerializer(serializers.Serializer):
    class Meta:
        model = GPUInfoModel
        fields = "__all__"
        read_only_fields = ["id"]


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = "__all__"
        read_only_fields = ["id"]
