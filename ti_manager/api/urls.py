from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('test-viewset',views.TestViewSet, basename='test-viewset')

urlpatterns = [
    path('hello-view/',views.HelloapiView.as_view()),
    path('test-view', include(router.urls)),
]