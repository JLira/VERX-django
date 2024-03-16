from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from brain_ag.produtor.urls import produtor_router
from brain_ag.fazenda.urls import fazenda_router
from brain_ag.cultura.urls import cultura_router

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test API brain_ag",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls')),

    #Produtor
    path('api/v1/', include(produtor_router.urls)),
    #Fazenda
    path('api/v1/', include(fazenda_router.urls)),
    #Cultura
    path('api/v1/', include(cultura_router.urls)),
]

#swagger
urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  

]