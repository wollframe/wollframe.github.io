from django.contrib import admin
from .models import *

class OrderAdmin (admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'distance', 'departure', 'published')
    list_display_links = ('name', 'phone_number', 'distance')
    search_fields = ('name', 'phone_number')



admin.site.register(Order, OrderAdmin)
