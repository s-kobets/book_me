from django.shortcuts import render
from django.views import generic
from .models import Event

# path('', ListView.as_view(queryset=Event.objects.all().order_by('-date'), template_name='events/index.html'), name='list'),
class EventsView(generic.ListView):
    model = Event
    template_name = 'events/list.html'
    # queryset = Event.objects.all().order_by('-date')
    # queryset = Event.objects.prefetch_related('carrier')

class EventView(generic.DetailView):
    model = Event
    template_name = 'events/event.html'