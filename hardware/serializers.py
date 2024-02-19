from rest_framework import serializers

from hardware.models import CPUInfo, Computer, GPUInfo

class CPUInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    frequency = serializers.FloatField()

class GPUInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    memory = serializers.IntegerField()

class ComputerSerializer(serializers.ModelSerializer):
    cpu = CPUInfoSerializer()
    gpu = GPUInfoSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Computer
        fields = ["id", "cpu", "gpu"]
        read_only_fields = ["id"]
    
    def create(self, validated_data):
        cpu_info = validated_data.get('cpu')
        gpu_info = validated_data.get('gpu')
        
        cpu = CPUInfo.objects.get_or_create(**cpu_info)[0]
        gpu = GPUInfo.objects.get_or_create(**gpu_info)[0] if gpu_info else None

        return Computer.objects.get_or_create(cpu=cpu, gpu=gpu)[0]
