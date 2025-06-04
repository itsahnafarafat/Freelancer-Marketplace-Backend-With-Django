from django.urls import path
from .views import (
    FreelancerProfileView,
    ClientProfileView,
    FreelancerDashboardView,
    ClientDashboardView,
)

urlpatterns = [
    path('freelancer/profile/', FreelancerProfileView.as_view(), name='freelancer-profile'),
    path('client/profile/', ClientProfileView.as_view(), name='client-profile'),
    path('freelancer/dashboard/', FreelancerDashboardView.as_view(), name='freelancer-dashboard'),
    path('client/dashboard/', ClientDashboardView.as_view(), name='client-dashboard'),
]
