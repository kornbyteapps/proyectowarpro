from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.base.general_api_view import GeneralListApiView
from apps.tickets.models import TicketCategory,TicketUrgency,TicketArea
from apps.tickets.api.serializers.general_serializer import TicketCategorySerializer,TicketUrgencySerializer,TicketAreaSerializer

class TicketCategoryListApiViewSet(viewsets.GenericViewSet):
    serializer_class = TicketCategorySerializer
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()
    
    def list(self,request):
        ticket_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(ticket_serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        '''
        Crea una categoria para tickets

        parametros.
        id = category_id
        desciption = descipción de la categoría ej: frontend, backend
        '''
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'categoria creada con exito' },status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            ticket_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if ticket_serializer.is_valid():
                ticket_serializer.save()
                return Response(ticket_serializer.data,status = status.HTTP_200_OK)
            return Response(ticket_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        ticket = self.get_queryset().filter(id = pk).first()
        if ticket:
            ticket.state = False
            ticket.save()
            return Response({'message':'Categoria eliminada correctamente'})
        return Response({'error':'No existe una categoría con estos datos'})
class TicketUrgencyListApiViewSet(viewsets.ModelViewSet):
    serializer_class = TicketUrgencySerializer
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()

class TicketAreaListApiViewSet(viewsets.ModelViewSet):
    serializer_class = TicketAreaSerializer
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()