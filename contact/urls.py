from django.urls import path
from .views import ContactMessageCreateView, CompanyContactInfoView

urlpatterns = [
    path('', ContactMessageCreateView.as_view(), name='contact-submit'),
    path('info', CompanyContactInfoView.as_view(), name='contact-info'),
]
