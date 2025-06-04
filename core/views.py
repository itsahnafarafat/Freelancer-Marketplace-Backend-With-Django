from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import FreelancerProfile, ClientProfile
from .serializers import FreelancerProfileSerializer, ClientProfileSerializer

# Freelance Profile
class FreelancerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'freelancer':
            return Response(
                {"error": "Only users with role 'freelancer' can create a freelancer profile."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = FreelancerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Client Profile
class ClientProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'client':
            return Response(
                {"error": "Only users with role 'client' can create a client profile."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = ClientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Freelance Dashboard
class FreelancerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'freelancer':
            return Response(
                {"error": "Only freelancers can create a freelancer profile."},
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {"message": f"Welcome to the Freelancer Dashboard, {request.user.email}!"},
            status=status.HTTP_200_OK
        )

# Client Dashboard
class ClientDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role !='client':
            return Response(
                {"error": "Only clients can create a client profile"}
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {"message": f"Welcome to the Client Dashboard, {request.user.email}!"},
            status=status.HTTP_200_OK
        )