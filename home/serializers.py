from rest_framework import serializers
from .models import (
    HeroSection,
    Service,
    WhyChooseUsReason,
    InfrastructureSection,
    ClientPage,
    ClientLogo
)

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class WhyChooseUsReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUsReason
        fields = '__all__'

class InfrastructureSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureSection
        fields = '__all__'

class ClientLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLogo
        fields = '__all__'

class ClientPageSerializer(serializers.ModelSerializer):
    logos = ClientLogoSerializer(many=True, read_only=True)

    class Meta:
        model = ClientPage
        fields = ['id', 'title', 'description', 'logos']
