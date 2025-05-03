import nested_admin
from django.contrib import admin
from .models import GalleryPage, GalleryItem

class GalleryItemInline(nested_admin.NestedTabularInline):
    model = GalleryItem
    extra = 1

@admin.register(GalleryPage)
class GalleryPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [GalleryItemInline]

    def has_add_permission(self, request):
        # Only allow one GalleryPage entry
        return not GalleryPage.objects.exists()
