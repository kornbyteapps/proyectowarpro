from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from apps.tickets.api.views.ticket_views import TicketViewSet
from apps.tickets.api.views.general_views import *
router = DefaultRouter()
router.register(r'tickets',TicketViewSet,basename='tickets'),
router.register(r'tickets-category',TicketCategoryListApiViewSet,basename='tickets-category'),
router.register(r'tickets-urgency',TicketUrgencyListApiViewSet,basename='tickets-urgency'),
router.register(r'tickets-area',TicketAreaListApiViewSet,basename='tickets-area'),

urlpatterns = router.urls