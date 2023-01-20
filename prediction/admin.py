from django.contrib import admin
from django.contrib.auth.models import Group
from prediction.models import *
from django.contrib.auth.models import AbstractUser, User
# Register your models here.

class PredictionTableAdmin(admin.ModelAdmin):
    list_display = ('Age', 'Sex', 'Excessive_urine','Excessive_thirst', 'Itching', 'Irritability', 'Hair_loss', 'Obesity')
    search_fields = ['Excessive_urine', 'Excessive_thirst']

class UserAdmin(admin.ModelAdmin):
    list_display = ('gender', 'phone', 'username')
    

    
admin.site.unregister(Group)
admin.site.register(User,UserAdmin)
admin.site.register(PredictionTable, PredictionTableAdmin)