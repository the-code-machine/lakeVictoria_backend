from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import HeroSection
from .serializers import HeroSectionSerializer

@api_view(['GET'])
def hero_section_view(request):
    try:
        hero = HeroSection.objects.first()  # assuming a single entry
        if hero:
            serializer = HeroSectionSerializer(hero)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No Hero Section found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
