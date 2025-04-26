from django.contrib import admin
from .models import HeroSection, Service, WhyChooseUsReason, InfrastructureFeature, InfrastructureSection, ClientPartner

admin.site.register(HeroSection)
admin.site.register(Service)
admin.site.register(WhyChooseUsReason)
admin.site.register(InfrastructureFeature)
admin.site.register(InfrastructureSection)
admin.site.register(ClientPartner)
