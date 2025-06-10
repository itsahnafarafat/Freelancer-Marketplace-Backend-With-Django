from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import JobPost, Application
from .serializers import JobPostSerializer, ApplicationSerializer
from .permissions import IsClient, IsFreelancer, IsOwnerOrReadOnly

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

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

    def get_permissions(self):
        if self.action == 'create':
            return [IsFreelancer()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user)
