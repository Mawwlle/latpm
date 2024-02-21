from rest_framework import generics, mixins, viewsets

from hardware.models import Computer, CPUInfo, CPUMonitoring, GPUInfo
from hardware.serializers import (ComputerSerializer, CPUInfoSerializer,
                                  CPUMonitoringSerializer, GPUInfoSerializer)


class ComputerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ComputerSerializer
    queryset = Computer.objects.all()


class CPUMonitoringViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CPUMonitoringSerializer
    queryset = CPUMonitoring.objects.all()


class CPUInfoViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = CPUInfoSerializer
    queryset = CPUInfo.objects.all()


class CPUInfoRetrieveView(generics.RetrieveAPIView):
    serializer_class = CPUInfoSerializer
    queryset = CPUInfo.objects.all()
    lookup_field = "name"


class GPUInfoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GPUInfoSerializer
    queryset = GPUInfo.objects.all()
