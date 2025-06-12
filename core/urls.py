from django.urls import path
from .views import RegisterView, LoginView, ClientDashboardView, FreelancerDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/client/', ClientDashboardView.as_view(), name='client-dashboard'),
    path('dashboard/freelancer/', FreelancerDashboardView.as_view(), name='freelancer-dashboard'),
]
