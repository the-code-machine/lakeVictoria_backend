# serializers.py
from rest_framework import serializers
from .models import CustomerMainPage, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'logo', 'description']

class CustomerMainPageSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer(many=True, read_only=True)

    class Meta:
        model = CustomerMainPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'customers']
