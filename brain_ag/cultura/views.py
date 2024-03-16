from brain_ag.cultura.models import Cultura
from brain_ag.cultura.serializers import CulturaSerializer
from rest_framework import viewsets

from rest_framework.response import Response


class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        total_culturas = queryset.count()
        data = {
            "culturas": serializer.data,
            "total_cultura": total_culturas
        }
        return Response(data)
