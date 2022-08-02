from django.urls import URLPattern, path, include
from apps.tickets.api.views.general_views import TicketCategoryListApiView,TicketUrgencyListApiView,TicketAreaListApiView
from apps.tickets.api.views.ticket_views import TicketListApiView,TicketListCreateApiView,TicketRetrieveUpdateDestroyApiView
urlpatterns =[
    path('ticket_catergory/',TicketCategoryListApiView.as_view(),name='measure_unit'),
    path('ticket_urgency/',TicketUrgencyListApiView.as_view(),name='indicator'),
    path('ticket_area/',TicketAreaListApiView.as_view(),name='category_tickets'),


]