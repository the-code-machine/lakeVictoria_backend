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

class VesselOverviewItemInline(nested_admin.NestedTabularInline):
    model = VesselOverviewItem
    extra = 1

class VesselCrewStatInline(nested_admin.NestedTabularInline):
    model = VesselCrewStat
    extra = 1

# --- Automation Admin ---
class AutomationSystemInline(nested_admin.NestedStackedInline):
    model = AutomationSystem
    inlines = [AutomationSystemFeatureInline]
    extra = 1

@admin.register(AutomationPage)
class AutomationPageAdmin(nested_admin.NestedModelAdmin):
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
    inlines = [LoadingBayInline, LoadingProcessStepInline, TruckLoadingSafetyInline]

# --- Vessel Admin ---
class VesselFeatureInline(nested_admin.NestedTabularInline):
    model = VesselFeature
    extra = 1

class VesselSpecInline(nested_admin.NestedTabularInline):
    model = VesselSpec
    extra = 1

class VesselCrewInline(nested_admin.NestedStackedInline):
    model = VesselCrew
    inlines = [VesselCrewStatInline]
    max_num = 1
    can_delete = False

@admin.register(VesselPage)
class VesselPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [VesselOverviewItemInline, VesselFeatureInline, VesselSpecInline, VesselCrewInline]
