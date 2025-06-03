from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    FreelancerProfileSerializer,
    ClientProfileSerializer
)
from .models import FreelancerProfile, ClientProfile

# Registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# Login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    
# Freelancer profile creation
class FreelanceProfileView(generics.CreateAPIView):
    serializer_class = FreelancerProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Client profile creation
class ClientProfileView(generics.CreateAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes =[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)