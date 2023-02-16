from django.urls import path
from general_app import views

urlpatterns = [
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]