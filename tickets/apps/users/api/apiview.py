from django.shortcuts import get_object_or_404
from django.urls import is_valid_path
from matplotlib.style import context
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.api.serializers import UserSerializer,UserListSerializer,UpdateUserSerializer

class UserViewset(viewsets.GenericViewSet):
    model = User
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self,pk):
        return get_object_or_404(self.model,pk=pk)

    def get_queryset(self):
        
        if self.queryset is None:
            self.queryset = self.model.objects.filter(activo = True).values('id','username','name','last_name','email')
        return self.queryset

    def list(self,request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users,many=True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario creado con exito'},status= status.HTTP_201_CREATED)
        return Response({'message':'Error en el registro','errors':user_serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data,)
    
    def put(self,request,pk=None):
        user = self.get_object(pk)
        print(user.activo)
        user_serializer = UpdateUserSerializer(user,data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario actualizado correctamente'},status = status.HTTP_200_OK)
        return Response({'message':'error usuario no encntrado','errors':user_serializer.errors},status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(activo=False)
        if user_destroy==1:
            return Response({'message':'Usuario eliminado correctamente'},status=status.HTTP_200_OK)
        return Response({'message':'No existe el usuario que desea eliminar'},status=status.HTTP_400_BAD_REQUEST) 