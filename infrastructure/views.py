from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class InfrastructureCombinedView(APIView):
    def get(self, request):
        return Response({
            "automation": AutomationPageSerializer(AutomationPage.objects.first()).data,
            "fire": FirePageSerializer(FirePage.objects.first()).data,
            "power": PowerPageSerializer(PowerPage.objects.first()).data,
            "storage": StoragePageSerializer(StoragePage.objects.first()).data,
            "truck_loading": TruckLoadingPageSerializer(TruckLoadingPage.objects.first()).data,
            "vessel": VesselPageSerializer(VesselPage.objects.first()).data,
        })
