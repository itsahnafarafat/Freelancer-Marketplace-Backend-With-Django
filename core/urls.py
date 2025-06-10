from django.urls import path
from .views import (
    JobPostListCreateView,
    JobPostDetailView,
    ApplicationCreateView,
    ApplicationListView,
)

urlpatterns = [
    path('jobs/', JobPostListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobPostDetailView.as_view(), name='job-detail'),
    path('jobs/<int:pk>/apply/', ApplicationCreateView.as_view(), name='job-apply'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
]
