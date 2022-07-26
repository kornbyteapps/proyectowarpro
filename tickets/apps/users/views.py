from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from datetime import datetime
from requests import session
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.api.serializers import CustomTokenObtainSerializer, CustomUserSerializer
from apps.users.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
    def post(self,request,*args,**kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(username = username, password=password)
        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token':login_serializer.validated_data.get('access'),
                    'refresh-token':login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message':'Inicio de sesión exitoso'
                },status = status.HTTP_200_OK)
            else:
                return Response({'error':'Contraseña o Usuario Incorrectos'},status.HTTP_400_BAD_REQUEST)
        else: return Response({'error':'Contraseña o Usuario Incorrectos'},status=status.HTTP_401_UNAUTHORIZED)
class Logout(GenericAPIView):
    def post(self,request,*args,**kwargs):
        user = User.objects.filter(id=request.data.get('user',))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Session cerrada correctamente'},status=status.HTTP_200_OK)
        return Response({'error':'No existe este Usuario'},status.HTTP_400_BAD_REQUEST)

'''class UserToken(APIView):
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializers().Meta.model.objects.filter(username=username).first()
            )
            return Response({'token':user_token.key})
        except:
            return Response({'error':'credenciales enviadas incorrectas'},status =status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data=request.data,context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializers(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesión exitoso'
                        }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token,created = Token.objects.get_or_create(user = user)
                    return  Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesión exitoso'
                        }, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Este usuario está inactivo'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Usuario o contraseña incorrectos'},status = status.HTTP_400_BAD_REQUEST)
        

class Logout(APIView):
    def post(self,request,*args,**kwargs):
        try:    
            token = request.POST.get('token')
            token = Token.objects.filter(key = token).first()
        
            if token:
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesión de usuario finalizada'
                token_message = 'Token eliminado'
                return Response({'token_message':token_message,'session_message':session_message},status = status.HTTP_200_OK)
            else:
                return Response({'error':'No se ha encontrado un usuario con estas credenciales'},status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'No se ha encontrado token en la petición'},status = status.HTTP_409_CONFLICT)'''

    