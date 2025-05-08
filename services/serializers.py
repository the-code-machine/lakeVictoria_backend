# serializers.py
from rest_framework import serializers
from .models import (
    ServiceMainPage, ServiceCategory, ServiceCategoryContent,
    LogisticServicePage, LogisticService, ServiceDetailPoint,
    ServiceAreaPage, CoverageMap, CountryCoverage, CountryLocation,
    ServiceAreaSection, ServiceAreaDetailPoint,
    StorageServicePage, StorageService, StorageServiceDetail
)

# --- Service Main Page ---
class ServiceCategoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategoryContent
        fields = ['sub_title', 'text']

class ServiceCategorySerializer(serializers.ModelSerializer):
    content_items = ServiceCategoryContentSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = [ 'title', 'description', 'image',  'content_items']

class ServiceMainPageSerializer(serializers.ModelSerializer):
    categories = ServiceCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ServiceMainPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'categories']


# --- Logistic Services ---
class ServiceDetailPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetailPoint
        fields = ['text']

class LogisticServiceSerializer(serializers.ModelSerializer):
    details = ServiceDetailPointSerializer(many=True, read_only=True)

    class Meta:
        model = LogisticService
        fields = [ 'title', 'description', 'image', 'details']

class LogisticServicePageSerializer(serializers.ModelSerializer):
    services = LogisticServiceSerializer(many=True, read_only=True)

    class Meta:
        model = LogisticServicePage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'image', 'services']


# --- Service Area ---
class CountryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryLocation
        fields = ['name']

class CountryCoverageSerializer(serializers.ModelSerializer):
    locations = CountryLocationSerializer(many=True, read_only=True)

    class Meta:
        model = CountryCoverage
        fields = ['country', 'locations']

class CoverageMapSerializer(serializers.ModelSerializer):
    countries = CountryCoverageSerializer(many=True, read_only=True)

    class Meta:
        model = CoverageMap
        fields = ['title', 'description', 'image', 'alt', 'countries']

class ServiceAreaDetailPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAreaDetailPoint
        fields = ['text']

class ServiceAreaSectionSerializer(serializers.ModelSerializer):
    details = ServiceAreaDetailPointSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceAreaSection
        fields = [ 'title', 'description', 'image', 'details']

class ServiceAreaPageSerializer(serializers.ModelSerializer):
    coverage_map = CoverageMapSerializer(read_only=True)
    sections = ServiceAreaSectionSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceAreaPage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'image', 'coverage_map', 'sections']


# --- Storage Services ---
class StorageServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageServiceDetail
        fields = ['text']

class StorageServiceSerializer(serializers.ModelSerializer):
    details = StorageServiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = StorageService
        fields = [ 'title', 'description', 'image', 'details']

class StorageServicePageSerializer(serializers.ModelSerializer):
    services = StorageServiceSerializer(many=True, read_only=True)

    class Meta:
        model = StorageServicePage
        fields = ['title', 'description', 'intro_title', 'intro_description', 'image', 'services']
