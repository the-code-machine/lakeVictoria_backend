# admin.py
from django.contrib import admin
from .models import CustomerMainPage, Customer
import nested_admin

class CustomerInline(nested_admin.NestedTabularInline):
    model = Customer
    extra = 1

@admin.register(CustomerMainPage)
class CustomerMainPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [CustomerInline]

    def has_add_permission(self, request):
        return not CustomerMainPage.objects.exists()