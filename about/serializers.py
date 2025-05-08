from rest_framework import serializers
from .models import *

# --- About Us ---
class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'

class AboutMainSerializer(serializers.ModelSerializer):
    sections = AboutSectionSerializer(many=True, read_only=True)

    class Meta:
        model = AboutMain
        fields = ['id', 'title', 'description', 'sections']


# --- About Company ---
class AboutCompanySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanySection
        fields = '__all__'

class AboutCompanyMainSerializer(serializers.ModelSerializer):
    sections = AboutCompanySectionSerializer(many=True, read_only=True)

    class Meta:
        model = AboutCompanyMain
        fields = ['id', 'title', 'description', 'sections']


# --- Environmental ---
class EnvironmentalBlockPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalBlockPoint
        fields = ['text']

class EnvironmentalBlockSerializer(serializers.ModelSerializer):
    points = EnvironmentalBlockPointSerializer(many=True, read_only=True)

    class Meta:
        model = EnvironmentalBlock
        fields = '__all__'

class EnvironmentalPillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalPillar
        fields = '__all__'

class EnvironmentalPageSerializer(serializers.ModelSerializer):
    blocks = EnvironmentalBlockSerializer(many=True, read_only=True)
    pillars = EnvironmentalPillarSerializer(many=True, read_only=True)

    class Meta:
        model = EnvironmentalPage
        fields = ['hero_title', 'hero_description', 'intro', 'blocks', 'pillars']


# --- Management Team ---
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class ManagementTeamPageSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(many=True, read_only=True)

    class Meta:
        model = ManagementTeamPage
        fields = ['title', 'description', 'members']


# --- Milestone ---
class FoundingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundingPoint
        fields = ['text']

class FoundingStorySerializer(serializers.ModelSerializer):
    points = FoundingPointSerializer(many=True, read_only=True)

    class Meta:
        model = FoundingStory
        fields = '__all__'

class MilestoneEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneEvent
        fields = '__all__'

class MilestoneAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneAchievement
        fields = '__all__'

class MilestonePageSerializer(serializers.ModelSerializer):
    timeline = MilestoneEventSerializer(many=True, read_only=True)
    achievements = MilestoneAchievementSerializer(many=True, read_only=True)
    founding_story = FoundingStorySerializer(read_only=True)

    class Meta:
        model = MilestonePage
        fields = ['hero_title', 'hero_description', 'intro', 'founding_story', 'timeline', 'achievements']


# --- Vision Mission ---
class VisionMissionPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionMissionPoint
        fields = ['text']

class VisionMissionBlockSerializer(serializers.ModelSerializer):
    points = VisionMissionPointSerializer(many=True, read_only=True)

    class Meta:
        model = VisionMissionBlock
        fields = '__all__'

class CompanyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyValue
        fields = '__all__'

class VisionMissionPageSerializer(serializers.ModelSerializer):
    blocks = VisionMissionBlockSerializer(many=True, read_only=True)
    values = CompanyValueSerializer(many=True, read_only=True)

    class Meta:
        model = VisionMissionPage
        fields = ['hero_title', 'hero_description', 'intro', 'blocks', 'values']


# --- Safety Policy ---
class SafetyPolicyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyPolicyItem
        fields = '__all__'

class SafetyPolicyPageSerializer(serializers.ModelSerializer):
    policies = SafetyPolicyItemSerializer(many=True, read_only=True)

    class Meta:
        model = SafetyPolicyPage
        fields = ['hero_title', 'hero_description', 'intro', 'policies']

# --- Investment (Refactored like Environment) ---
class InvestmentBlockPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentBlockPoint
        fields = ['text']

class InvestmentBlockSerializer(serializers.ModelSerializer):
    points = InvestmentBlockPointSerializer(many=True, read_only=True)

    class Meta:
        model = InvestmentBlock
        fields = '__all__'

class InvestmentPageSerializer(serializers.ModelSerializer):
    blocks = InvestmentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = InvestmentPage
        fields = ['hero_title', 'hero_description', 'intro', 'blocks', ]
