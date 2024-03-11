from django.shortcuts import render
from .models import Fazenda
from .serializers import FazendaSerializer
from rest_framework import viewsets
from rest_framework import permissions


class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer
