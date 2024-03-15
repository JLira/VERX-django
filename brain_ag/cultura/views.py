from rest_framework import generics
from brain_ag.cultura.models import Cultura
from brain_ag.cultura.serializers import CulturaSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer

    @swagger_auto_schema(
        operation_summary="Lista todas as culturas",
        operation_description="Esta view retorna uma lista de todas as culturas.",
        responses={200: CulturaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)