from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import FreelancerProfile, ClientProfile
from .serializers import FreelancerProfileSerializer, ClientProfileSerializer

class FreelancerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'freelancer':
            return Response(
                {"error": "Only freelancers can create a freelancer profile."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = FreelancerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClientProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role !='client':
            return Response(
                {"error": "Only clients can create a client profile"}
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = ClientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)