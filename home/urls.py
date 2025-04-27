from django.urls import path
from .views import hero_section_view

urlpatterns = [
    path('api/hero-section/', hero_section_view, name='hero-section'),
]
