
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apps.users.views import Login,Logout

schema_view = get_schema_view(
    openapi.Info(
        title = 'Warpro Tickets Api Documentation',
        default_version = 'v0.1',
        description='Documentación api rest Help Desk',
        terms_of_service="https://helpdeskapipoliciyservice.com",
        contact=openapi.Contact(email = 'develop@warpro.cl'),
        licence= openapi.License(name = 'BSD Licence')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docu/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.routers')),
    path('tickets/',include('apps.tickets.api.routers')),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]
