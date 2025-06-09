from django.urls import path
from .views import InfrastructureCombinedView, vessel_fleet_view, individual_vessel_view

urlpatterns = [
    path('', InfrastructureCombinedView.as_view(), name='infrastructure-all'),
    path('vessel-fleet/', vessel_fleet_view, name='vessel-fleet'),
    path('vessel/<int:vessel_id>/', individual_vessel_view, name='individual-vessel'),
]
