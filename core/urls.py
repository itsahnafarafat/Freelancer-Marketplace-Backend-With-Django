from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet, ApplicationViewSet

router = DefaultRouter()
router.register('jobs', JobPostViewSet, basename='jobpost')
router.register('applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]
