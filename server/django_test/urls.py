"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
import notifications.urls

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Prussian API",
        default_version='v1',
        description="Prussian API description",
        terms_of_service="",
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pauth/', include('pauth.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('administration/', include('apps.administration.urls', namespace="administration")),
    path('business/', include('apps.business.urls', namespace="business")),
    path('market/', include('apps.market.urls', namespace="market")),
    path('user/', include('apps.user_setting.urls',  namespace="user")),
    path('',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema_swagger_ui'),
    path('json/',
         schema_view.without_ui(cache_timeout=0),
         name='schema_json'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema_redoc'),
]
