from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MediaEventsPage, MediaArticle, Event
from .serializers import (
    MediaEventsPageSerializer,
    MediaArticleSerializer,
    EventSerializer
)

class MediaEventsCombinedView(APIView):
    def get(self, request):
        # Get the main page (assuming only one exists)
        media_page = MediaEventsPage.objects.first()
        media_page_data = MediaEventsPageSerializer(media_page).data if media_page else {}

        # Get all articles
        articles = MediaArticle.objects.all().order_by('-date')
        articles_data = MediaArticleSerializer(articles, many=True).data

        # Get all events
        events = Event.objects.all().order_by('-date')
        events_data = EventSerializer(events, many=True).data

        return Response({
            "main_info": media_page_data,
            "media_articles": articles_data,
            "events": events_data
        })
