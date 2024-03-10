from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Produtor
from .serializers import ProdutorSerializer


class ProdutorAPIView(APIView):
    """
       API de produtor
    """

    def get(self, request):
        produtor = Produtor.objects.all()
        serializer = ProdutorSerializer(produtor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
