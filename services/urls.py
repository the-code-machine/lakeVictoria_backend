from django.urls import path
from .views import AllServicesView

urlpatterns = [
    path('', AllServicesView.as_view(), name='services_api'),
]