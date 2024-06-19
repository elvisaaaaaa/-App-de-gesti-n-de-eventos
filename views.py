from django.shortcuts import render, get_object_or_404
from .models import Venue, Event, Ticket, Registration

def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/event_list.html',
