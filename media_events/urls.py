from django.urls import path
from .views import MediaEventsCombinedView

urlpatterns = [
    path('', MediaEventsCombinedView.as_view(), name='media-events-combined'),
]
