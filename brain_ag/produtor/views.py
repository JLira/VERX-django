from rest_framework import generics
from .models import Produtor
from .serializers import ProdutorSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import EhSuperUser


"""
API V1
"""


class ProdutoresAPIView(generics.ListCreateAPIView):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer


class ProdutorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer


"""
API V2
"""


class ProdutorViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
