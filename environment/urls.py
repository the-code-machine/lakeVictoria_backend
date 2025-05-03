from django.urls import path
from .views import AllEnvironmentalDataView

urlpatterns = [
    path('', AllEnvironmentalDataView.as_view(), name='environmental-page'),
]
