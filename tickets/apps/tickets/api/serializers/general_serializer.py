from apps.tickets.models import TicketUrgency,TicketArea,TicketCategory
from rest_framework import serializers

class TicketCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = TicketCategory
        exclude =('state','created_date','modified_date','deleted_date',)

class TicketAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketArea
        exclude =('state','created_date','modified_date','deleted_date',)

class TicketUrgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketUrgency
        exclude =('state','created_date','modified_date','deleted_date',)
