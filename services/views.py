
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
class AllServicesView(APIView):
    def get(self, request):
        service_main = ServiceMainPage.objects.first()
        logistics = LogisticServicePage.objects.first()
        area = ServiceAreaPage.objects.first()
        storage = StorageServicePage.objects.first()

        return Response({
            "service_main": ServiceMainPageSerializer(service_main).data,
            "logistics": LogisticServicePageSerializer(logistics).data,
            "area": ServiceAreaPageSerializer(area).data,
            "storage": StorageServicePageSerializer(storage).data,
        })
