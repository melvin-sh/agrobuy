from django.contrib import admin
from farmer.models import Farmer 


# Register your models here.


@admin.register(Farmer)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','address','mobile']

