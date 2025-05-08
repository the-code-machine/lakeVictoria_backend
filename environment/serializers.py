from rest_framework import serializers
from .models import (
    EnvironmentalPage, EnvironmentalInitiative,
    CarbonFootprintPage,
    OilManagementPage, OilSystem, OilProcessStep
)

class EnvironmentalInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalInitiative
        fields = ['id', 'title', 'description', 'image', 'stats']  # Removed 'link'

class EnvironmentalPageSerializer(serializers.ModelSerializer):
    initiatives = EnvironmentalInitiativeSerializer(many=True, read_only=True)

    class Meta:
        model = EnvironmentalPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'image', 'initiatives']

class CarbonFootprintPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonFootprintPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'image', 'volume_shipped']

class OilSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilSystem
        fields = ['id', 'title', 'description', 'efficiency', 'image']

class OilProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilProcessStep
        fields = ['step', 'title', 'description']

class OilManagementPageSerializer(serializers.ModelSerializer):
    systems = OilSystemSerializer(many=True, read_only=True)
    process_steps = OilProcessStepSerializer(many=True, read_only=True)

    class Meta:
        model = OilManagementPage
        fields = ['title', 'description', 'image', 'volume_shipped', 'systems', 'process_steps']
