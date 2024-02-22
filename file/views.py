from django.http import StreamingHttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.request import Request

from benchmark.models import BenchmarkModel
from file.models import DatasetModel
from hardware.models import CPUInfoModel


class RequestSerializer(serializers.Serializer):
    table = serializers.ListField()


@extend_schema(
    request=[RequestSerializer],
    responses={
        status.HTTP_200_OK: StreamingHttpResponse,
    },
)
@api_view(["POST"])
def generate_csv(request: Request) -> StreamingHttpResponse:
    model_mapper = {"cpu": CPUInfoModel, "benchmark": BenchmarkModel}
    serializer = RequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    tables = serializer.data["table"]
    qss = [model_mapper[table].objects.all() for table in tables]
    dataset = DatasetModel.objects.create_with_concat(query_sets=qss)

    response = StreamingHttpResponse(dataset.csvfile, content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(
        dataset.csvfile.name
    )
    return response
