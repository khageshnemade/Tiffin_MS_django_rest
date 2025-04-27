"""
URL configuration for tiffin_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include,re_path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.views import CustomTokenObtainPairView

schema_view = get_schema_view(
   openapi.Info(
      title="Tiffin Management Service API",
      default_version='v1',
      description="API documentation for Tiffin Management Service",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[JWTAuthentication],   # 👈 important
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',CustomTokenObtainPairView.as_view(),name='token_obtain_pair'),#login
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),#refresh_token
    path('api/accounts/',include('accounts.urls')),#signup and register
    path('hotel/',include('hotels.urls')),
    path('order/',include('orders.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  
    
]
