from django.contrib.auth import get_user_model
from numpy import isin
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import User

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','name','last_name')

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('username','email','name','last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    def update(self,instance,validated_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nombre-usuario':instance['username'],
            'nombre': instance['name'],
            'apellido': instance['last_name'],
            'email': instance['email']
            
        }

class showCurrentUserProfileSerializer(serializers.ModelSerializer):
    User = get_user_model()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',     
        ]

'''class TestUserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    
    def validate_name(self,value):
        #custom validation
        if'developer' in value:
            raise serializers.ValidationError('No puede existir un user con ese nombre')
        return value
    def validate_email(self, value):
        if value=='':
            raise serializers.ValidationError('El campo email no puede estar vacío')
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('Email no puede contener el nombre de usuario')
        #if value in users_serializer:
        #    raise serializers.ValidationError('El email ya existe ')
        return value
    def validate(self, data):
        return data
    def create(self,validated_data):
        #Using Django ORM to insert in bd
        return User.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.username = validated_data.get('username',instance.username)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance'''