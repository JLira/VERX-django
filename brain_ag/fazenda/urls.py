from django.urls import path

from rest_framework.routers import SimpleRouter

from brain_ag.fazenda.views import FazendaViewSet

fazenda_router = SimpleRouter()
fazenda_router.register('fazendas', FazendaViewSet)

urlpatterns = []
