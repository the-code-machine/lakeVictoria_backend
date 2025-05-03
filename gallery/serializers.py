# serializers.py
from rest_framework import serializers
from .models import GalleryPage, GalleryItem

class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = ['id', 'src', 'caption', 'date', 'type', 'thumbnail']

class GalleryPageSerializer(serializers.ModelSerializer):
    items = GalleryItemSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'image', 'items']
