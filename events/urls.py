from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView, DetailView
from .models import Event
from . import views, api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', api.EventViewSet, 'event')

urlpatterns = [
    path('', views.EventsView.as_view(), name='list'),
    path('<int:pk>/', views.EventView.as_view(), name='detail'),
    path('api/', include(router.urls)),
]
