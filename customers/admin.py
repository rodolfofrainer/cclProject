from django.contrib import admin
from .models import Customers

# Register your models here.

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name', 'socialMedia']
    list_per_page = 20
    list_display = ['name', 'socialMedia', 'date_created']