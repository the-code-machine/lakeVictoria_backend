from django.contrib import admin
from .models import (
    MediaEventsPage, MediaSection,
    MediaArticle, Event, EventImage
)

# Inline for MediaSection inside MediaEventsPage
class MediaSectionInline(admin.TabularInline):
    model = MediaSection
    extra = 1

@admin.register(MediaEventsPage)
class MediaEventsPageAdmin(admin.ModelAdmin):
    inlines = [MediaSectionInline]
    list_display = ['title']
    search_fields = ['title', 'intro_title']

@admin.register(MediaArticle)
class MediaArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication', 'date']
    search_fields = ['title', 'publication']
    list_filter = ['publication', 'date']
    ordering = ['-date']

# Inline for EventImage inside Event
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    list_display = ['title', 'event_id', 'date', 'location']
    search_fields = ['title', 'event_id', 'location']
    list_filter = ['date', 'location']
    ordering = ['-date']
