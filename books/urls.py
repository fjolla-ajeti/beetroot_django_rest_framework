from django.urls import path
from .views import HomeBookView


urlpatterns = [
    path('', HomeBookView.as_view(), name='home'),  # Shtoni këtë URL pattern për faqen fillestare
]


