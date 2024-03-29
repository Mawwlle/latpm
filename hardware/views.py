from rest_framework import generics, mixins, viewsets

from hardware.models import (ComputerModel, CPUInfoModel, CPUMonitoringModel,
                             GPUInfoModel)
from hardware.serializers import (ComputerSerializer, CPUInfoSerializer,
                                  CPUMonitoringSerializer, GPUInfoSerializer)


class ComputerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ComputerSerializer
    queryset = ComputerModel.objects.all()


class CPUMonitoringViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CPUMonitoringSerializer
    queryset = CPUMonitoringModel.objects.all()


class CPUInfoViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = CPUInfoSerializer
    queryset = CPUInfoModel.objects.all()


class CPUInfoRetrieveView(generics.RetrieveAPIView):
    serializer_class = CPUInfoSerializer
    queryset = CPUInfoModel.objects.all()
    lookup_field = "name"


class GPUInfoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GPUInfoSerializer
    queryset = GPUInfoModel.objects.all()
