from rest_framework import generics
from .models import Cultura
from .serializers import CulturaSerializer
from rest_framework import viewsets

class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer
