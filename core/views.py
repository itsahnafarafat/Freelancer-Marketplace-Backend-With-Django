from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import JobPost, Application
from .serializers import JobPostSerializer, ApplicationSerializer
from .permissions import IsClient, IsFreelancer
from django.db.models import Q

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.freelancerprofile.role == 'client':
            return JobPost.objects.filter(client=user)
        return JobPost.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsClient()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.freelancerprofile.role == 'freelancer':
            return Application.objects.filter(freelancer=user)
        return Application.objects.none()

    def get_permissions(self):
        if self.action == 'create':
            return [IsFreelancer()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user)
