from news.models import Event, Action, Tag, EventAction
from django.shortcuts import render

def index(request):
    """View function for home page of site."""

    events = Event.objects.all()
    tags = Tag.objects.all()
    actions_count = Action.objects.all().count()
    event_actions = EventAction.objects.values()


    context = {
        'actions_count': actions_count,
        'events': events,
        'tags': tags,
        'event_actions': event_actions
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)
