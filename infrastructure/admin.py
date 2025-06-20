# infrastructure/admin.py
import nested_admin
from django.contrib import admin
from .models import *

# --- Generic Inlines for Text Blocks ---
class AutomationBenefitInline(nested_admin.NestedTabularInline):
    model = AutomationBenefit
    extra = 1

class AutomationSystemFeatureInline(nested_admin.NestedTabularInline):
    model = AutomationSystemFeature
    extra = 1

class FireOverviewItemInline(nested_admin.NestedTabularInline):
    model = FireOverviewItem
    extra = 1

class FireSystemFeatureInline(nested_admin.NestedTabularInline):
    model = FireSystemFeature
    extra = 1

class FireTrainingItemInline(nested_admin.NestedTabularInline):
    model = FireTrainingItem
    extra = 1

class PowerDistributionFeatureInline(nested_admin.NestedTabularInline):
    model = PowerDistributionFeature
    extra = 1

class StorageTankFeatureInline(nested_admin.NestedTabularInline):
    model = StorageTankFeature
    extra = 1

class TruckLoadingSafetyPointInline(nested_admin.NestedTabularInline):
    model = TruckLoadingSafetyPoint
    extra = 1

class TruckLoadingEfficiencyPointInline(nested_admin.NestedTabularInline):
    model = TruckLoadingEfficiencyPoint
    extra = 1


# --- Automation Admin ---
class AutomationSystemInline(nested_admin.NestedStackedInline):
    model = AutomationSystem
    inlines = [AutomationSystemFeatureInline]
    extra = 1

@admin.register(AutomationPage)
class AutomationPageAdmin(nested_admin.NestedModelAdmin):
    def has_add_permission(self, request):
        return not AutomationPage.objects.exists()
    inlines = [AutomationBenefitInline, AutomationSystemInline]

# --- Fire Admin ---
class FireSystemInline(nested_admin.NestedStackedInline):
    model = FireSystem
    inlines = [FireSystemFeatureInline]
    extra = 1

class FireTrainingInline(nested_admin.NestedStackedInline):
    model = FireTraining
    inlines = [FireTrainingItemInline]
    max_num = 1
    can_delete = False

class AutoModeStepInline(nested_admin.NestedTabularInline):
    model = AutoModeStep
    extra = 1

@admin.register(FirePage)
class FirePageAdmin(nested_admin.NestedModelAdmin):
    def has_add_permission(self, request):
        return not FirePage.objects.exists()
    inlines = [FireOverviewItemInline, FireSystemInline, AutoModeStepInline, FireTrainingInline]

# --- Power Admin ---
class PowerSystemInline(nested_admin.NestedTabularInline):
    model = PowerSystem
    extra = 1

class PowerDistributionInline(nested_admin.NestedStackedInline):
    model = PowerDistribution
    inlines = [PowerDistributionFeatureInline]
    max_num = 1
    can_delete = False

class PowerMaintenanceStepInline(nested_admin.NestedTabularInline):
    model = PowerMaintenanceStep
    extra = 1

@admin.register(PowerPage)
class PowerPageAdmin(nested_admin.NestedModelAdmin):
    def has_add_permission(self, request):
        return not PowerPage.objects.exists()
    inlines = [PowerSystemInline, PowerDistributionInline, PowerMaintenanceStepInline]

# --- Storage Admin ---
class StorageTankInline(nested_admin.NestedStackedInline):
    model = StorageTank
    inlines = [StorageTankFeatureInline]
    extra = 1

class StorageSafetyBlockInline(nested_admin.NestedTabularInline):
    model = StorageSafetyBlock
    extra = 1

@admin.register(StoragePage)
class StoragePageAdmin(nested_admin.NestedModelAdmin):
    def has_add_permission(self, request):
        return not StoragePage.objects.exists()
    inlines = [StorageTankInline, StorageSafetyBlockInline]

# --- Truck Loading Admin ---
class LoadingBayInline(nested_admin.NestedTabularInline):
    model = LoadingBay
    extra = 1

class LoadingProcessStepInline(nested_admin.NestedTabularInline):
    model = LoadingProcessStep
    extra = 1

class TruckLoadingSafetyInline(nested_admin.NestedStackedInline):
    model = TruckLoadingSafety
    inlines = [TruckLoadingSafetyPointInline, TruckLoadingEfficiencyPointInline]
    max_num = 1
    can_delete = False

@admin.register(TruckLoadingPage)
class TruckLoadingPageAdmin(nested_admin.NestedModelAdmin):
    def has_add_permission(self, request):
        return not TruckLoadingPage.objects.exists()
    inlines = [LoadingBayInline, LoadingProcessStepInline, TruckLoadingSafetyInline]

# --- Updated Vessel Admin Configuration ---

class VesselImageInline(nested_admin.NestedTabularInline):
    model = VesselImage
    extra = 1
    fields = ['image', 'caption', 'order']

class VesselFeatureInline(nested_admin.NestedTabularInline):
    model = VesselFeature
    extra = 1
    fields = ['feature_id', 'title', 'description', 'order']

class VesselSpecInline(nested_admin.NestedTabularInline):
    model = VesselSpec
    extra = 1
    fields = ['label', 'value', 'type', 'order']

class VesselCrewStatInline(nested_admin.NestedTabularInline):
    model = VesselCrewStat
    extra = 1
    fields = ['label', 'desc', 'order']

class VesselCrewInline(nested_admin.NestedStackedInline):
    model = VesselCrew
    inlines = [VesselCrewStatInline]
    max_num = 1
    can_delete = False
    fields = ['title', 'summary']

class IndividualVesselInline(nested_admin.NestedStackedInline):
    model = IndividualVessel
    inlines = [VesselImageInline, VesselFeatureInline, VesselSpecInline, VesselCrewInline]
    extra = 0
    fields = ['name', 'description', 'main_image', 'is_active', 'order']

@admin.register(VesselFleetPage)
class VesselFleetPageAdmin(nested_admin.NestedModelAdmin):
    def has_add_permission(self, request):
        return not VesselFleetPage.objects.exists()
    
    inlines = [IndividualVesselInline]
    fields = ['title', 'description', 'intro_title', 'intro_text']

@admin.register(IndividualVessel)
class IndividualVesselAdmin(nested_admin.NestedModelAdmin):
    list_display = ['name', 'fleet_page', 'is_active', 'order']
    list_filter = ['is_active', 'fleet_page']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'description']
    
    inlines = [VesselImageInline, VesselFeatureInline, VesselSpecInline, VesselCrewInline]
    fields = ['fleet_page', 'name', 'description', 'main_image', 'is_active', 'order']