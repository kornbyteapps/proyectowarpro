from django.db import models
from rest_framework import serializers
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.users.models import User

# Create your models here.
class TicketUrgency(BaseModel):
    description = models.CharField('Descripción',max_length=50,blank=False,null=False, unique=True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Urgencia del ticket'
        verbose_name_plural = 'Urgencia de los tickets'
    def __str__(self):
        return self.description

class TicketCategory(BaseModel):
    description = models.CharField('Descripción',max_length=50,blank=False,null=False, unique=True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de ticket'
        verbose_name_plural = 'Categorias de los tickets'
    def __str__(self):
        return self.description

class TicketArea(BaseModel):
    description = models.CharField('Descripción',max_length=50,blank=False,null=False, unique=True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Area del ticket'
        verbose_name_plural = 'Area de los tickets'
    def __str__(self):
        return self.description

class Ticket(BaseModel):
    ticket_category = models.ForeignKey(TicketCategory,on_delete=models.CASCADE,verbose_name='Categoria de ticket',null=True)
    ticket_urgency = models.ForeignKey(TicketUrgency, on_delete = models.CASCADE, verbose_name='Urgencia del ticket',null=True)
    ticket_area = models.ForeignKey(TicketArea,on_delete=models.CASCADE,verbose_name='Area de ticket',null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name='id usuario',null=True)
    subject = models.CharField('Asunto del ticket',max_length=150,blank = False, unique = False, null = False)
    description = models.TextField('Descripción de producto',blank=False,null=False)
    image = models.ImageField('Imagen del producto', upload_to = 'products/',blank = True, null = True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    def __str__(self):
        return self.subject

# Create your models here.
