from django import views
from django.urls import URLPattern, path, include
from apps.users.api.apiview import UserApiView
from apps.users.api.apiview import user_api_view,user_datail_api_view,ShowCurrentUserProfileApiView
urlpatterns =[
    #path('usuario/',UserApiView.as_view(),name='usuario_api'),
    path('user/', user_api_view, name='usuario'),
    path('user/<int:pk>', user_datail_api_view, name='usuario_detail'),
    path('current-user', ShowCurrentUserProfileApiView.as_view(),name='loged-user-details'),
    
]