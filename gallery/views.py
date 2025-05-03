# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GalleryPage
from .serializers import GalleryPageSerializer

class GalleryPageView(APIView):
    def get(self, request):
        page = GalleryPage.objects.first()
        serializer = GalleryPageSerializer(page)
        return Response(serializer.data)