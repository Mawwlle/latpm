from rest_framework import serializers

from hardware.models import Computer, CPUInfo, CPUMonitoring, GPUInfo


class CPUInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUInfo
        fields = "__all__"
        read_only_fields = ["id"]


class CPUMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUMonitoring
        fields = "__all__"
        read_only_fields = ["id"]


class GPUInfoSerializer(serializers.Serializer):
    class Meta:
        model = GPUInfo
        fields = "__all__"
        read_only_fields = ["id"]


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = "__all__"
        read_only_fields = ["id"]
