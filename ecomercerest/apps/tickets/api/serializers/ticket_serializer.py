from apps.tickets.models import Ticket
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    #measure_unit = serializers.StringRelatedField()
    #category_product = serializers.StringRelatedField()
    class Meta:
        model = Ticket
        exclude = ('state','created_date','modified_date','deleted_date',)
    def to_representation(self, instance):
        return {
            'ticket_id': instance.id,
            'user_id':instance.user.id if instance.user.id is not None else '',
            'user_name':instance.user.name,
            'subject': instance.subject,
            'description':instance.description,
            #'image':instance.image if instance.image != '' else '',
            'ticket_category':instance.ticket_category.description if instance.ticket_category is not None else '',
            'ticket_urgency':instance.ticket_urgency.description if instance.ticket_urgency is not None else '',
            'ticket_area':instance.ticket_area.description if instance.ticket_area is not None else '',
        }