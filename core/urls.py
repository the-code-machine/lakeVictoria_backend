
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),  # required
    path('', include('home.urls')),  # add this
    path('about/', include('about.urls')),  # add this
    path('services/', include('services.urls')),  # add this
    path('contact/', include('contact.urls')),  # add this
    path('our_customer/', include('our_customer.urls')),  # add this
    path('gallery/', include('gallery.urls')),  # add this
    path('environment/', include('environment.urls')),  # add this
    path('media_events/', include('media_events.urls')),  # add this
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)