# admin.py
from django.contrib import admin
from .models import (
    EnvironmentalPage, EnvironmentalInitiative,
    CarbonFootprintPage,
    OilManagementPage, OilSystem, OilProcessStep
)

class EnvironmentalInitiativeInline(admin.TabularInline):
    model = EnvironmentalInitiative
    extra = 1

@admin.register(EnvironmentalPage)
class EnvironmentalPageAdmin(admin.ModelAdmin):
    inlines = [EnvironmentalInitiativeInline]

@admin.register(CarbonFootprintPage)
class CarbonFootprintPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not CarbonFootprintPage.objects.exists()

class OilSystemInline(admin.TabularInline):
    model = OilSystem
    extra = 1

class OilProcessStepInline(admin.TabularInline):
    model = OilProcessStep
    extra = 1

@admin.register(OilManagementPage)
class OilManagementPageAdmin(admin.ModelAdmin):
    inlines = [OilSystemInline, OilProcessStepInline]