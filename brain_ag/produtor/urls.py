from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import ProdutorAPIView, ProdutoresAPIView, ProdutorViewSet

router = SimpleRouter()
router.register('produtores', ProdutorViewSet)

urlpatterns = [
    path('produtores/', ProdutoresAPIView.as_view(), name='produtores'),
    path('produtores/<uuid:pk>/', ProdutorAPIView.as_view(), name='produtor')
]
