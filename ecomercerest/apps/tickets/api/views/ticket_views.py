
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.base.general_api_view import GeneralListApiView
from apps.tickets.api.serializers.ticket_serializer import TicketSerializer
from apps.users.authentication_mixin import Authentication

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()
    
    def list(self,request):
        ticket_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(ticket_serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Ticket creado con exito' },status= status.HTTP_201_CREATED)
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
            return Response({'message':'Ticket eliminado correctamente'})
        return Response({'error':'No existe un Ticket con estos datos'})

    


'''class TicketListApiView(GeneralListApiView):
    serializer_class = TicketSerializer

class TicketListCreateApiView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = TicketSerializer.Meta.model.objects.filter(state=True)
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Ticket creado con exito' },status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)'''

'''class TicketRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            ticket_serialiazer = self.serializer_class(self.get_queryset(pk))
            return Response(ticket_serialiazer.data,status = status.HTTP_200_OK)
        return Response({'error':'No existe un Ticket con estos datos'})'''

    

    
    
    


    