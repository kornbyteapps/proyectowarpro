from matplotlib.style import context
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from apps.users.models import User
from apps.users.api.serializers import UserSerializer,UserListSerializer,showCurrentUserProfileSerializer

class UserApiView(APIView):
    def get(self,request):
        users = User.objects.all()
        users_serializer = UserSerializer(users,many=True)

        return Response(users_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])        
def user_api_view(request):
    #List All
    if request.method =='GET':
        #queryset
        users = User.objects.all().values('id','username','last_name','email','password')
        users_serializer = UserListSerializer(users,many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    #create
    elif request.method == 'POST':
        #queryset
        user_serializer = UserSerializer(data = request.data)
        #validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        else: return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def user_datail_api_view(request,pk=None):
    #queryset
    user = User.objects.filter(id=pk).first()
    #validacion
    if user:
        #retrieve
        if request.method =='GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        #update
        elif request.method == 'PUT': 
            user_serializer = UserSerializer(instance = user,data = request.data,context = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else: return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method =='DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'}, status = status.HTTP_200_OK)
    else: return Response({'message':'No se ha encontrado un usario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

class ShowCurrentUserProfileApiView(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		serializer = showCurrentUserProfileSerializer(request.user)
		return Response(serializer.data)    
'''******************SERIALIZER INSERT TEST **************************************'''
'''test_data = {
        'username':'sebaaaastddiandevaddaeloper',
        'name':'sebastian',
        'last_name':'pascal',
        'email':'sebaaaaaaaasddddawwwwa@gmail.com'
        }
    test_user = TestUserSerializer(data = test_data, context=test_data)
    if test_user.is_valid():
        #print('Pasó la validación')
        user_instance = test_user.save()
            
    else: print(test_user.errors)'''
'''********************************************************'''