from django.contrib import admin
from .models import Mobile

# Register your models here.
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'model', 'price']