from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import (
    HeroSection,
    Service,
    WhyChooseUsReason,
    InfrastructureSection,
    ClientPage
)

from .serializers import (
    HeroSectionSerializer,
    ServiceSerializer,
    WhyChooseUsReasonSerializer,
    InfrastructureSectionSerializer,
    ClientPageSerializer
)


@api_view(['GET'])
def home_page_view(request):
    try:
        # Fetch individual objects
        hero = HeroSection.objects.first()
        why_choose_us = WhyChooseUsReason.objects.first()
        infrastructure = InfrastructureSection.objects.first()
        client_page = ClientPage.objects.first()
        services = Service.objects.all()[:4]  # limit to 4 services

        data = {
            "hero_section": HeroSectionSerializer(hero).data if hero else None,
            "services": ServiceSerializer(services, many=True).data,
            "why_choose_us": WhyChooseUsReasonSerializer(why_choose_us).data if why_choose_us else None,
            "infrastructure": InfrastructureSectionSerializer(infrastructure).data if infrastructure else None,
            "clients": ClientPageSerializer(client_page).data if client_page else None
        }

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
