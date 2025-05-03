from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EnvironmentalPage, CarbonFootprintPage, OilManagementPage
from .serializers import (
    EnvironmentalPageSerializer,
    CarbonFootprintPageSerializer,
    OilManagementPageSerializer,
)

class AllEnvironmentalDataView(APIView):
    def get(self, request):
        data = {
            "environmental": EnvironmentalPageSerializer(EnvironmentalPage.objects.first()).data,
            "carbon_footprint": CarbonFootprintPageSerializer(CarbonFootprintPage.objects.first()).data,
            "oil_management": OilManagementPageSerializer(OilManagementPage.objects.first()).data,
        }
        return Response(data)
