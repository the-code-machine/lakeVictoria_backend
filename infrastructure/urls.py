from django.urls import path
from .views import InfrastructureCombinedView

urlpatterns = [
    path('', InfrastructureCombinedView.as_view(), name='infrastructure-all'),
]
