from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ContactMessage, CompanyContactInfo
from .serializers import (
    ContactMessageSerializer,
    CompanyContactInfoSerializer,
)

# --- Contact form submission view ---
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

# --- Public-facing company info + business team ---
class CompanyContactInfoView(APIView):
    def get(self, request):
        try:
            info = CompanyContactInfo.objects.prefetch_related('contacts').first()
            serializer = CompanyContactInfoSerializer(info)
            return Response(serializer.data)
        except CompanyContactInfo.DoesNotExist:
            return Response({"detail": "Contact information not available"}, status=404)
