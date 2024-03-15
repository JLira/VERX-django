from django.urls import path

from rest_framework.routers import SimpleRouter


from brain_ag.produtor.views import  ProdutorViewSet

produtor_router = SimpleRouter()
produtor_router.register('produtores', ProdutorViewSet)

urlpatterns = []
