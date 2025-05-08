# infrastructure/serializers.py
from rest_framework import serializers
from .models import *

# --- Block Serializers ---
class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = ['text']

class AutomationBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomationBenefit
        fields = ['text']

class AutomationSystemFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomationSystemFeature
        fields = ['text']

class FireSystemFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireSystemFeature
        fields = ['text']

class FireTrainingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireTrainingItem
        fields = ['text']

class FireOverviewItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireOverviewItem
        fields = ['text']

class PowerDistributionFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerDistributionFeature
        fields = ['text']

class StorageTankFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageTankFeature
        fields = ['text']

class TruckLoadingSafetyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckLoadingSafetyPoint
        fields = ['text']

class TruckLoadingEfficiencyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckLoadingEfficiencyPoint
        fields = ['text']

class VesselOverviewItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselOverviewItem
        fields = ['text']

# -------- Automation --------
class AutomationSystemSerializer(serializers.ModelSerializer):
    features = AutomationSystemFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = AutomationSystem
        fields = ['system_id', 'title', 'description', 'features', 'image']

class AutomationPageSerializer(serializers.ModelSerializer):
    benefits = AutomationBenefitSerializer(many=True, read_only=True)
    systems = AutomationSystemSerializer(many=True, read_only=True)

    class Meta:
        model = AutomationPage
        fields = ['title', 'description', 'intro_title', 'intro_description',
                  'overview_title', 'overview_description', 'benefits_title',
                  'benefits', 'overview_image', 'systems']

# -------- Fire --------
class FireSystemSerializer(serializers.ModelSerializer):
    features = FireSystemFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = FireSystem
        fields = ['system_id', 'title', 'description', 'features', 'image']

class AutoModeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoModeStep
        fields = ['step', 'title', 'description']

class FireTrainingSerializer(serializers.ModelSerializer):
    items = FireTrainingItemSerializer(many=True, read_only=True)

    class Meta:
        model = FireTraining
        fields = ['title', 'description', 'items', 'image']

class FirePageSerializer(serializers.ModelSerializer):
    systems = FireSystemSerializer(many=True, read_only=True)
    auto_mode_steps = AutoModeStepSerializer(many=True, read_only=True)
    training = FireTrainingSerializer(read_only=True)
    overview_items = FireOverviewItemSerializer(many=True, read_only=True)

    class Meta:
        model = FirePage
        fields = ['title', 'description', 'intro_title', 'intro_text',
                  'overview_title', 'overview_text', 'list_title',
                  'overview_items', 'overview_image',
                  'systems', 'auto_mode_steps', 'training']

# -------- Power --------
class PowerSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSystem
        fields = ['system_id', 'title', 'description', 'capacity', 'response_time', 'image']

class PowerDistributionSerializer(serializers.ModelSerializer):
    features = PowerDistributionFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = PowerDistribution
        fields = ['title', 'heading', 'text', 'features', 'image']

class PowerMaintenanceStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerMaintenanceStep
        fields = ['step', 'title', 'description']

class PowerPageSerializer(serializers.ModelSerializer):
    systems = PowerSystemSerializer(many=True, read_only=True)
    maintenance_steps = PowerMaintenanceStepSerializer(many=True, read_only=True)
    distribution = PowerDistributionSerializer(read_only=True)

    class Meta:
        model = PowerPage
        fields = ['title', 'description', 'intro_title', 'intro_text',
                  'critical_systems', 'systems', 'distribution', 'maintenance_steps']

# -------- Storage --------
class StorageTankSerializer(serializers.ModelSerializer):
    features = StorageTankFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = StorageTank
        fields = ['tank_id', 'name', 'capacity', 'type', 'product', 'features', 'image']

class StorageSafetyBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageSafetyBlock
        fields = ['title', 'text']

class StoragePageSerializer(serializers.ModelSerializer):
    tanks = StorageTankSerializer(many=True, read_only=True)
    safety_blocks = StorageSafetyBlockSerializer(many=True, read_only=True)

    class Meta:
        model = StoragePage
        fields = ['title', 'description', 'intro_title', 'intro_prefix', 'intro_suffix', 'tanks', 'safety_blocks']

# -------- Truck Loading --------
class LoadingBaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadingBay
        fields = ['bay_id', 'name', 'product_type', 'loading_rate']

class LoadingProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadingProcessStep
        fields = ['step', 'title', 'description']

class TruckLoadingSafetySerializer(serializers.ModelSerializer):
    safety_points = TruckLoadingSafetyPointSerializer(many=True, read_only=True)
    efficiency_points = TruckLoadingEfficiencyPointSerializer(many=True, read_only=True)

    class Meta:
        model = TruckLoadingSafety
        fields = ['title', 'safety_points', 'efficiency_points']

class TruckLoadingPageSerializer(serializers.ModelSerializer):
    bays = LoadingBaySerializer(many=True, read_only=True)
    process_steps = LoadingProcessStepSerializer(many=True, read_only=True)
    safety = TruckLoadingSafetySerializer(read_only=True)

    class Meta:
        model = TruckLoadingPage
        fields = ['title', 'description', 'intro_title', 'config_note', 'average_rate',
                  'truck_count', 'intro_image', 'bays', 'process_steps', 'safety']

# -------- Vessel Fleet --------
class VesselFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselFeature
        fields = ['feature_id', 'title', 'description']

class VesselSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselSpec
        fields = ['label', 'value', 'type']

class VesselCrewStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselCrewStat
        fields = ['label', 'desc']

class VesselCrewSerializer(serializers.ModelSerializer):
    stats = VesselCrewStatSerializer(many=True, read_only=True)

    class Meta:
        model = VesselCrew
        fields = ['title', 'summary', 'stats']

class VesselPageSerializer(serializers.ModelSerializer):
    overview_items = VesselOverviewItemSerializer(many=True, read_only=True)
    features = VesselFeatureSerializer(many=True, read_only=True)
    specs = VesselSpecSerializer(many=True, read_only=True)
    crew = VesselCrewSerializer(read_only=True)

    class Meta:
        model = VesselPage
        fields = ['title', 'description', 'intro_title', 'intro_text',
                  'overview_title', 'overview_text', 'overview_items', 'overview_image',
                  'features', 'specs', 'crew']