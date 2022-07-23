from django.contrib import admin
from apps.products.models import *
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description')
#print(MeasureUnitAdmin)

class CategoryPorductAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(MeasureUnit)
admin.site.register(CategoryProduct)
admin.site.register(Indicator)
admin.site.register(Product)

# Register your models here.
