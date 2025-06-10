from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
class InfrastructureCombinedView(APIView):
    def get(self, request):
        return Response({
            "automation": AutomationPageSerializer(AutomationPage.objects.first()).data,
            "fire": FirePageSerializer(FirePage.objects.first()).data,
            "power": PowerPageSerializer(PowerPage.objects.first()).data,
            "storage": StoragePageSerializer(StoragePage.objects.first()).data,
            "truck_loading": TruckLoadingPageSerializer(TruckLoadingPage.objects.first()).data,
         
        })

@api_view(['GET'])
def vessel_fleet_view(request):
    """API endpoint for vessel fleet overview with all vessels"""
    try:
        fleet_page = VesselFleetPage.objects.prefetch_related(
            'vessels__additional_images'
        ).get()
        serializer = VesselFleetPageSerializer(fleet_page)
        return Response({'vessel_fleet': serializer.data})
    except VesselFleetPage.DoesNotExist:
        return Response({'error': 'Vessel fleet page not found'}, status=404)

@api_view(['GET'])
def individual_vessel_view(request, vessel_id):
    """API endpoint for individual vessel details"""
    vessel = get_object_or_404(
        IndividualVessel.objects.prefetch_related(
            'additional_images',
            'features',
            'specs',
            'crew_info__stats'
        ),
        id=vessel_id,
        is_active=True
    )
    serializer = IndividualVesselSerializer(vessel)
    return Response({'vessel': serializer.data})
