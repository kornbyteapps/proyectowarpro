import datetime
from django.db import models
from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class users(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=(100))
    creation_date =models.DateField()
    active = models.BooleanField(default=True)

    

class UserProfileManager(BaseUserManager):
    #Manager para perfiles de usuario
    def create_user(self, email, password=None):
        #nuevo user profile
        if not email:
            raise ValueError('Usuario debe tener email')
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return(user)

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #modelo base de datos para usuarios del sistema
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIERED_FIELDS = ['name']

    def get_full_name(self):
        #nombre completo suer
        return self.name
    def get_short_name(self):
        #nombre corte user
        return self.name

    def __str__(self):
        #cadena q representa el usuario
        return self.email
# Create your models here.
