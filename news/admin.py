from django.contrib import admin

# Register your models here.
from .models import Event, Article, Tag, Action, SpamAction, EventAction, EventTag, WatchedEvent, UserVote
admin.site.register(Event)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Action)
admin.site.register(SpamAction)
admin.site.register(EventAction)
admin.site.register(EventTag)
admin.site.register(WatchedEvent)
admin.site.register(UserVote)
