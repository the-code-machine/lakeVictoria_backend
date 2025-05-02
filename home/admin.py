from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import (
    HeroSection,
    Service,
    WhyChooseUsReason,
    InfrastructureSection,
    ClientPage,
    ClientLogo
)

# --- INLINE FOR LOGOS ---
class ClientLogoInline(admin.TabularInline):
    model = ClientLogo
    extra = 1

# --- CLIENT PAGE ADMIN ---
@admin.register(ClientPage)
class ClientPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ClientLogoInline]

# Remove the ClientLogoAdmin registration to hide it from the admin panel
# ClientLogo will only be managed through the ClientLogoInline in ClientPageAdmin

# --- SINGLE INSTANCE ENFORCEMENT ---
class SingleInstanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding more than one instance
        return not self.model.objects.exists()

# --- HERO SECTION ---
@admin.register(HeroSection)
class HeroSectionAdmin(SingleInstanceAdmin):
    list_display = ('title', 'years_experience', 'countries_served', 'support_hours')

# --- WHY CHOOSE US SECTION ---
@admin.register(WhyChooseUsReason)
class WhyChooseUsReasonAdmin(SingleInstanceAdmin):
    list_display = ('title',)

# --- INFRASTRUCTURE SECTION ---
@admin.register(InfrastructureSection)
class InfrastructureSectionAdmin(SingleInstanceAdmin):
    list_display = ('title',)

# --- SERVICE SECTION (max 4 instances) ---
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        # Allow up to 4 service entries
        if self.model.objects.count() >= 4:
            return False
        return super().has_add_permission(request)
