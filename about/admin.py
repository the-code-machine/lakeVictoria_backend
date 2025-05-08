import nested_admin
from django.contrib import admin
from .models import *


# ---------- ABOUT MAIN ----------
class AboutSectionInline(admin.TabularInline):
    model = AboutSection
    extra = 1

@admin.register(AboutMain)
class AboutMainAdmin(admin.ModelAdmin):
    inlines = [AboutSectionInline]

    def has_add_permission(self, request):
        return not AboutMain.objects.exists()


# ---------- ABOUT COMPANY ----------
class AboutCompanySectionInline(admin.TabularInline):
    model = AboutCompanySection
    extra = 1

@admin.register(AboutCompanyMain)
class AboutCompanyMainAdmin(admin.ModelAdmin):
    inlines = [AboutCompanySectionInline]

    def has_add_permission(self, request):
        return not AboutCompanyMain.objects.exists()


# ---------- ENVIRONMENT ----------
class EnvironmentalBlockPointInline(nested_admin.NestedTabularInline):
    model = EnvironmentalBlockPoint
    extra = 1

class EnvironmentalBlockInline(nested_admin.NestedStackedInline):
    model = EnvironmentalBlock
    inlines = [EnvironmentalBlockPointInline]
    extra = 1

class EnvironmentalPillarInline(nested_admin.NestedTabularInline):
    model = EnvironmentalPillar
    extra = 1

@admin.register(EnvironmentalPage)
class EnvironmentalPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [EnvironmentalBlockInline, EnvironmentalPillarInline]

    def has_add_permission(self, request):
        return not EnvironmentalPage.objects.exists()


# ---------- MILESTONES ----------
class FoundingPointInline(nested_admin.NestedTabularInline):
    model = FoundingPoint
    extra = 1

class FoundingStoryInline(nested_admin.NestedStackedInline):
    model = FoundingStory
    inlines = [FoundingPointInline]
    extra = 0
    can_delete = False
    show_change_link = True

class MilestoneEventInline(nested_admin.NestedTabularInline):
    model = MilestoneEvent
    extra = 1

class MilestoneAchievementInline(nested_admin.NestedTabularInline):
    model = MilestoneAchievement
    extra = 1

@admin.register(MilestonePage)
class MilestonePageAdmin(nested_admin.NestedModelAdmin):
    inlines = [FoundingStoryInline, MilestoneEventInline, MilestoneAchievementInline]

    def has_add_permission(self, request):
        return not MilestonePage.objects.exists()


# ---------- VISION & MISSION ----------
class VisionMissionPointInline(nested_admin.NestedTabularInline):
    model = VisionMissionPoint
    extra = 1

class VisionMissionBlockInline(nested_admin.NestedStackedInline):
    model = VisionMissionBlock
    inlines = [VisionMissionPointInline]
    extra = 1

class CompanyValueInline(nested_admin.NestedTabularInline):
    model = CompanyValue
    extra = 1

@admin.register(VisionMissionPage)
class VisionMissionPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [VisionMissionBlockInline, CompanyValueInline]

    def has_add_permission(self, request):
        return not VisionMissionPage.objects.exists()


# ---------- INVESTMENT (Updated like ENVIRONMENT) ----------
class InvestmentBlockPointInline(nested_admin.NestedTabularInline):
    model = InvestmentBlockPoint
    extra = 1

class InvestmentBlockInline(nested_admin.NestedStackedInline):
    model = InvestmentBlock
    inlines = [InvestmentBlockPointInline]
    extra = 1


@admin.register(InvestmentPage)
class InvestmentPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [InvestmentBlockInline]

    def has_add_permission(self, request):
        return not InvestmentPage.objects.exists()


# ---------- SAFETY ----------
class SafetyPolicyItemInline(admin.TabularInline):
    model = SafetyPolicyItem
    extra = 1

@admin.register(SafetyPolicyPage)
class SafetyPolicyPageAdmin(admin.ModelAdmin):
    inlines = [SafetyPolicyItemInline]

    def has_add_permission(self, request):
        return not SafetyPolicyPage.objects.exists()


# ---------- TEAM ----------
class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

@admin.register(ManagementTeamPage)
class ManagementTeamPageAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]

    def has_add_permission(self, request):
        return not ManagementTeamPage.objects.exists()
