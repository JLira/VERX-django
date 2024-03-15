from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import CulturaViewSet

cultura_router = SimpleRouter()
cultura_router.register('culturas', CulturaViewSet)

urlpatterns = []
