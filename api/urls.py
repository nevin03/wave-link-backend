from django.urls import path
from .views import TermsView, PrivacyView, ContactDetailsView

urlpatterns = [
    path("terms/", TermsView.as_view(), name="terms"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("contact/", ContactDetailsView.as_view(), name="contact"),
]
