from news.models import Event, Action, Tag, EventAction
from django.shortcuts import render, get_object_or_404

def index(request):
    """View function for home page of site."""

    events = Event.objects.all()
    tags = Tag.objects.all()
    actions_count = Action.objects.all().count()
    actions = events.prefetch_related('actions')


    context = {
        'actions_count': actions_count,
        'events': events,
        'tags': tags,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})