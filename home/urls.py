from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('api/home_page/', home_page_view, name='home_page_view'),
]
