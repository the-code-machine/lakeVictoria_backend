import nested_admin
from django.contrib import admin
from .models import *

# ------------------------ Automation ------------------------
class AutomationSystemInline(nested_admin.NestedTabularInline):
    model = AutomationSystem
    extra = 1

@admin.register(AutomationPage)
class AutomationPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [AutomationSystemInline]
    list_display = ['title']


# ------------------------ Fire ------------------------
class FireSystemInline(nested_admin.NestedTabularInline):
    model = FireSystem
    extra = 1

class AutoModeStepInline(nested_admin.NestedTabularInline):
    model = AutoModeStep
    extra = 1

class FireTrainingInline(nested_admin.NestedStackedInline):
    model = FireTraining
    can_delete = False
    max_num = 1
    extra = 0

@admin.register(FirePage)
class FirePageAdmin(nested_admin.NestedModelAdmin):
    inlines = [FireSystemInline, AutoModeStepInline, FireTrainingInline]
    list_display = ['title']


# ------------------------ Power ------------------------
class PowerSystemInline(nested_admin.NestedTabularInline):
    model = PowerSystem
    extra = 1

class PowerMaintenanceStepInline(nested_admin.NestedTabularInline):
    model = PowerMaintenanceStep
    extra = 1

class PowerDistributionInline(nested_admin.NestedStackedInline):
    model = PowerDistribution
    can_delete = False
    max_num = 1
    extra = 0

@admin.register(PowerPage)
class PowerPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [PowerSystemInline, PowerMaintenanceStepInline, PowerDistributionInline]
    list_display = ['title']


# ------------------------ Storage ------------------------
class StorageTankInline(nested_admin.NestedTabularInline):
    model = StorageTank
    extra = 1

class StorageSafetyBlockInline(nested_admin.NestedTabularInline):
    model = StorageSafetyBlock
    extra = 1

@admin.register(StoragePage)
class StoragePageAdmin(nested_admin.NestedModelAdmin):
    inlines = [StorageTankInline, StorageSafetyBlockInline]
    list_display = ['title']


# ------------------------ Truck Loading ------------------------
class LoadingBayInline(nested_admin.NestedTabularInline):
    model = LoadingBay
    extra = 1

class LoadingProcessStepInline(nested_admin.NestedTabularInline):
    model = LoadingProcessStep
    extra = 1

class TruckLoadingSafetyInline(nested_admin.NestedStackedInline):
    model = TruckLoadingSafety
    can_delete = False
    max_num = 1
    extra = 0

@admin.register(TruckLoadingPage)
class TruckLoadingPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [LoadingBayInline, LoadingProcessStepInline, TruckLoadingSafetyInline]
    list_display = ['title']


# ------------------------ Vessel ------------------------
class VesselFeatureInline(nested_admin.NestedTabularInline):
    model = VesselFeature
    extra = 1

class VesselSpecInline(nested_admin.NestedTabularInline):
    model = VesselSpec
    extra = 1

class VesselCrewStatInline(nested_admin.NestedTabularInline):
    model = VesselCrewStat
    extra = 1

class VesselCrewInline(nested_admin.NestedStackedInline):
    model = VesselCrew
    extra = 0
    can_delete = False
    max_num = 1
    inlines = [VesselCrewStatInline]

@admin.register(VesselPage)
class VesselPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [VesselFeatureInline, VesselSpecInline, VesselCrewInline]
    list_display = ['title']
