from django.contrib import admin
from apps.tickets.models import *

class TicketCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','description')
#print(MeasureUnitAdmin)

class TicketUrgencyAdmin(admin.ModelAdmin):
    list_display = ('id','description')
class TicketAreaAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(TicketCategory)
admin.site.register(TicketUrgency)
admin.site.register(TicketArea)
admin.site.register(Ticket)
