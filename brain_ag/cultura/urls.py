from django.urls import path, include

# from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter
from .views import CulturaViewSet

# cultura_router = SimpleRouter()
# cultura_router.register('culturas', CulturaViewSet)

cultura_router = DefaultRouter()
cultura_router.register(prefix='culturas', viewset=CulturaViewSet, basename='culturas')

urlpatterns = [
    path('', include(cultura_router.urls))
]
