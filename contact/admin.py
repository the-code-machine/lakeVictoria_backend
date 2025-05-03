import nested_admin
from django.contrib import admin
from .models import ContactMessage, CompanyContactInfo, BusinessDevelopmentContact

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    readonly_fields = ('name', 'email', 'phone', 'message', 'submitted_at')
    search_fields = ('name', 'email')


class BusinessDevelopmentInline(nested_admin.NestedTabularInline):
    model = BusinessDevelopmentContact
    extra = 1


@admin.register(CompanyContactInfo)
class CompanyContactInfoAdmin(nested_admin.NestedModelAdmin):
    inlines = [BusinessDevelopmentInline]

    def has_add_permission(self, request):
        return not CompanyContactInfo.objects.exists()
