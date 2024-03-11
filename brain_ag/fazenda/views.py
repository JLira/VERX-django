from rest_framework.response import Response
from django.shortcuts import render
from .models import Fazenda
from .serializers import FazendaSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions


class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer

    # @action(detail=True, method=['get'])
    # def culturas(self, request, pk=None):
    #     fazenda = self.get_object()
    #     serializer = FazendaSerializer(fazenda.culturas.all(), many=True)
    #     return Response(serializer.data)
