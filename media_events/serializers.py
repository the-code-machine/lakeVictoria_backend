from rest_framework import serializers
from .models import (
    MediaEventsPage, MediaSection,
    MediaArticle, Event, EventImage
)

class MediaSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaSection
        fields = ['section_id', 'title', 'description', 'image',]

class MediaEventsPageSerializer(serializers.ModelSerializer):
    sections = MediaSectionSerializer(many=True, read_only=True)

    class Meta:
        model = MediaEventsPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'sections']

class MediaArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaArticle
        fields = ['title', 'publication', 'date', 'summary', 'image']

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['src', 'caption']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['event_id', 'title', 'date', 'description', 'location', 'thumbnail_image', 'images']
