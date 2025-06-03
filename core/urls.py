from django.urls import path
from .views import RegisterView, LoginView, FreelanceProfileView, ClientProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('freelancer/profile/', FreelanceProfileView.as_view(), name='freelancer-profile'),
    path('client/profile/', ClientProfileView.as_view(), name='client-profile'),
]