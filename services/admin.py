import nested_admin
from django.contrib import admin
from .models import *
class ServiceCategoryContentInline(nested_admin.NestedTabularInline):
    model = ServiceCategoryContent
    extra = 1


class ServiceCategoryInline(nested_admin.NestedStackedInline):
    model = ServiceCategory
    inlines = [ServiceCategoryContentInline]
    extra = 1


@admin.register(ServiceMainPage)
class ServiceMainPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [ServiceCategoryInline]

    def has_add_permission(self, request):
        return not ServiceMainPage.objects.exists()


class ServiceDetailPointInline(nested_admin.NestedTabularInline):
    model = ServiceDetailPoint
    extra = 1


class LogisticServiceInline(nested_admin.NestedStackedInline):
    model = LogisticService
    inlines = [ServiceDetailPointInline]
    extra = 1


@admin.register(LogisticServicePage)
class LogisticServicePageAdmin(nested_admin.NestedModelAdmin):
    inlines = [LogisticServiceInline]

    def has_add_permission(self, request):
        return not LogisticServicePage.objects.exists()

# --- Inline for Country Locations ---
class CountryLocationInline(nested_admin.NestedTabularInline):
    model = CountryLocation
    extra = 1


# --- Inline for each Country in the Coverage Map ---
class CountryCoverageInline(nested_admin.NestedStackedInline):
    model = CountryCoverage
    inlines = [CountryLocationInline]
    extra = 1


# --- Coverage Map Inline (OneToOne) ---
class CoverageMapInline(nested_admin.NestedStackedInline):
    model = CoverageMap
    inlines = [CountryCoverageInline]
    extra = 0
    can_delete = False
    show_change_link = True


# --- Inline for Detail Points under ServiceAreaSection ---
class ServiceAreaDetailPointInline(nested_admin.NestedTabularInline):
    model = ServiceAreaDetailPoint
    extra = 1


# --- Inline for ServiceAreaSection ---
class ServiceAreaSectionInline(nested_admin.NestedStackedInline):
    model = ServiceAreaSection
    inlines = [ServiceAreaDetailPointInline]
    extra = 1


# --- Register Main Page ---
@admin.register(ServiceAreaPage)
class ServiceAreaPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [CoverageMapInline, ServiceAreaSectionInline]

    def has_add_permission(self, request):
        return not ServiceAreaPage.objects.exists()

class StorageServiceDetailInline(nested_admin.NestedTabularInline):
    model = StorageServiceDetail
    extra = 1


class StorageServiceInline(nested_admin.NestedStackedInline):
    model = StorageService
    inlines = [StorageServiceDetailInline]
    extra = 1


@admin.register(StorageServicePage)
class StorageServicePageAdmin(nested_admin.NestedModelAdmin):
    inlines = [StorageServiceInline]

    def has_add_permission(self, request):
        return not StorageServicePage.objects.exists()