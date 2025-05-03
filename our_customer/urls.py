# urls.py
from django.urls import path
from .views import CustomerMainPageView

urlpatterns = [
    path('', CustomerMainPageView.as_view(), name='customer-main-page'),
]