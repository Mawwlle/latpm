from django.db import models


class CPUInfoModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    frequency = models.FloatField()
    arch = models.CharField(max_length=10)
    bits = models.IntegerField()
    count = models.IntegerField()
    l1_data_cache_size = models.IntegerField(null=True)
    l1_instruction_cache_size = models.IntegerField(null=True)
    l2_cache_size = models.IntegerField()
    l2_cache_line_size = models.IntegerField()
    l2_cache_associativity = models.IntegerField()
    l3_cache_size = models.IntegerField(null=True)
    stepping = models.IntegerField()
    model = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"


class CPUMonitoringModel(models.Model):
    cpu = models.ForeignKey(CPUInfoModel, on_delete=models.CASCADE)
    frequency_actual = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class GPUInfoModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    memory = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.memory}"


class ComputerModel(models.Model):
    cpu = models.ForeignKey(CPUInfoModel, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPUInfoModel, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"Computer with CPU: {self.cpu.name} and GPU: {getattr(self.gpu, 'name', 'N/A')}"
