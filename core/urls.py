from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    FreelancerProfileCreateView, 
    ClientProfileCreateView,
    FreelancerDashboardView,
    ClientDashboardView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('freelancer/profile/', FreelancerProfileCreateView.as_view(), name='freelancer-profile'),
    path('client/profile/', ClientProfileCreateView.as_view(), name='client-profile'),
    path('freelancer/dashboard/', FreelancerDashboardView.as_view(), name='freelancer-dashboard'),
    path('client/dashboard/', ClientDashboardView.as_view(), name='client-dashboard'),
]