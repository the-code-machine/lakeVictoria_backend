from django.urls import path
from .views import home_combined_view

urlpatterns = [
    path('', home_combined_view, name='home-combined'),
]
