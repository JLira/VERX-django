"""brain_ag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from brain_ag.produtor.urls import router
from brain_ag.fazenda.urls import fazenda_router
from brain_ag.cultura.urls import cultura_router

urlpatterns = [
    path('api/v1/', include('brain_ag.produtor.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls')),
    #Fazenda
    path('api/v2/', include(fazenda_router.urls)),
    #Cultura
    path('api/v2/', include(cultura_router.urls)),
]
