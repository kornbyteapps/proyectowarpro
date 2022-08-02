from email import message
from django.shortcuts import render
from rest_framework import status
from api import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

class HelloapiView(APIView):
    #clase de vista de api de prueba
    serializer_class = serializers.HelloSerializer  
    def get(self, request, format=None ):
        #retornar lista de caracteristicas del apiview
        an_apiview = [
            'usamos metodos http cmo funciones (get, post patch, put, delete)',
            'es Similar a una  vista tradicional de Django',
            'Nos da mejor control sobre la lógica de la app',
            'Esta mapeado manualmente a los URLS'
        ]
        return Response({'message':'Hello WORLD','an_apiview':an_apiview})
    def post(self,request):
        #crea un mensaje con nuestro nombre
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Holi{name}'
            return Response({'Mensaje':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        #update object
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        # PARTIAL update object
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        #delete object
        return Response({'method':'DELETE'})

class TestViewSet(viewsets.ViewSet):
    #test api viewset
    def list(self,request):
        a_viewset =[
            'Usa acciones List,retrieve,update,partialupdate',
            'Automaticamentemapea los URL',
            'Provee mas funcionalidad con menos código',
        ]
        return Response({'Test-msj':'Retornando lista a_viewset ','a_viewset':a_viewset})