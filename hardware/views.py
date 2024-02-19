from rest_framework import viewsets, mixins
from hardware.models import Computer

from hardware.serializers import ComputerSerializer

class ComputerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()
