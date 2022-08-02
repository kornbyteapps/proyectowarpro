from rest_framework.routers import DefaultRouter
from apps.users.api.apiview import UserViewset

router = DefaultRouter()
router.register('',UserViewset, basename='users')

urlpatterns = router.urls