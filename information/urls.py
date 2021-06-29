from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us', views.AboutUsView.as_view(), name='about_us'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('privacy', views.PrivacyView.as_view(), name='privacy'),
    path('terms', views.TermsView.as_view(), name='terms'),
]
