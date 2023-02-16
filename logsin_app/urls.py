from django.urls import path
from logsin_app import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('success/', views.success, name='success'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('changepassword/', views.changepassword, name='changepassword'),
]