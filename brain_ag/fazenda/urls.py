from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import FazendaViewSet

fazenda_router = SimpleRouter()
fazenda_router.register('fazendas', FazendaViewSet)

urlpatterns = [
    # path('fazendas/', FazendaViewSet.as_view(), name='fazendas'),
    # path('fazendas/<uuid:pk>/', FazendaViewSet.as_view(), name='fazenda')
]
