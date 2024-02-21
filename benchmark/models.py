from django.db import models


class Benchmark(models.Model):
    class Type(models.TextChoices):
        MULTIPROCESSING = "MP", "Multiprocessing"
        TORCH_TENSOR_OPERATIONS = "TTO", "Torch tensor operations"

    type = models.CharField(
        max_length=3,
        choices=Type.choices,
        default=Type.MULTIPROCESSING,
    )
    threads = models.PositiveIntegerField(default=1)
    result = models.FloatField()
    computer = models.ForeignKey(to="hardware.Computer", on_delete=models.CASCADE)
