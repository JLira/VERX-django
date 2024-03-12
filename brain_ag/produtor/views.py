from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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


    @action(detail=False, methods=['put'])
    def update_by_cpf(self, request, cpf):
        """
        Atualiza um produtor pelo CPF.
        """
        try:
            produtor = Produtor.objects.get(cpf=cpf)
        except Produtor.DoesNotExist:
            return Response({"detail": "Produtor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProdutorSerializer(produtor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)