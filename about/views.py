from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['GET'])
def home_combined_view(request):
    try:
        data = {}

        if (about := AboutMain.objects.first()):
            data["about"] = AboutMainSerializer(about).data

        if (company := AboutCompanyMain.objects.first()):
            data["about_company"] = AboutCompanyMainSerializer(company).data

        if (env := EnvironmentalPage.objects.first()):
            data["environment"] = EnvironmentalPageSerializer(env).data

        if (team := ManagementTeamPage.objects.first()):
            data["management"] = ManagementTeamPageSerializer(team).data

        if (milestone := MilestonePage.objects.first()):
            data["milestones"] = MilestonePageSerializer(milestone).data

        if (vm := VisionMissionPage.objects.first()):
            data["vision_mission"] = VisionMissionPageSerializer(vm).data

        if (safety := SafetyPolicyPage.objects.first()):
            data["safety_policies"] = SafetyPolicyPageSerializer(safety).data

        if (investment := InvestmentPage.objects.first()):
            data["investment"] = InvestmentPageSerializer(investment).data

        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
