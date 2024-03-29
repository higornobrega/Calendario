"""calendario URL Configuration

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
from django.urls import path, include, re_path
from rest_framework import routers
from Evento.api import viewsets as eventoviewsets
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Calendário",
      default_version='v1',
      description="Bem-vindo à documentação da API Calendário da UNIFIP \nNossa API tem como objetivo alimentar o calendário academico da UNIFIP com seus eventos e datas comemorativas.\n A API que falaremos nessa documentação é a v1, onde as datas são representadas. \nFornecemos endpoints com respostas apresentadas em formato JSON. \nUtilizamos o princípio REST, que é simples de integrar, eficiente e seguro.",
      contact=openapi.Contact(email="gerenciati@fiponline.edu.br"),
      license=openapi.License(name="Apache 2.0"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)


route = routers.DefaultRouter()

route.register(r'evento', eventoviewsets.EventoViewsets, basename="Evento")

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("", include(route.urls))
]