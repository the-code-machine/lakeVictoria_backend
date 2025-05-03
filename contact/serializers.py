from rest_framework import serializers
from .models import ContactMessage, CompanyContactInfo, BusinessDevelopmentContact

# --- Business Dev Contacts inside Company Info ---
class BusinessDevelopmentContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDevelopmentContact
        fields = ['name', 'title', 'email', 'phone']

# --- Company Info Serializer with nested business contacts ---
class CompanyContactInfoSerializer(serializers.ModelSerializer):
    contacts = BusinessDevelopmentContactSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyContactInfo
        fields = [
            'address_line1', 'address_line2', 'address_line3', 'address_line4',
            'phone', 'general_email', 'contacts'
        ]

# --- Contact Form Serializer ---
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
