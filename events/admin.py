from django.contrib import admin
from .models import Event, Place, Transport

admin.register(Event, Place, Transport)(admin.ModelAdmin)