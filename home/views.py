from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HeroSection
from .serializers import HeroSectionSerializer

@api_view(['GET'])
def hero_section_view(request):
    hero = HeroSection.objects.first()  # assuming only 1 HeroSection entry
    if hero:
        serializer = HeroSectionSerializer(hero)
        return Response(serializer.data)
    return Response({"detail": "No Hero Section found"}, status=404)
