# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomerMainPage
from .serializers import CustomerMainPageSerializer

class CustomerMainPageView(APIView):
    def get(self, request):
        main_page = CustomerMainPage.objects.prefetch_related('customers').first()
        if main_page:
            serializer = CustomerMainPageSerializer(main_page)
            return Response(serializer.data)
        return Response({"detail": "No data available."}, status=404)

