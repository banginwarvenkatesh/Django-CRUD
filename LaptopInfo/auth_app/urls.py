from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerView, name='reg_url'),
    path('login/', views.loginView, name='login_url'),
    path('logout/', views.logoutView, name='logout_url'),
    path('otp/', views.OTPview, name='otp_url')
]