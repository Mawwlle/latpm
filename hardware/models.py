from django.db import models

class CPUInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    frequency = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name} - {self.frequency}"

class GPUInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    memory = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} - {self.memory}"

class Computer(models.Model):
    cpu = models.ForeignKey(CPUInfo, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPUInfo, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"Computer with CPU: {self.cpu.name} and GPU: {getattr(self.gpu, 'name', 'N/A')}"
