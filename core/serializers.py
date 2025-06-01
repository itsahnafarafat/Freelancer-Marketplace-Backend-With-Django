from rest_framework import serializers
from .models import FreelancerProfile, ClientProfile

class FreelancerProfileSerializer(serializers, ModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = ['skills', 'experience']

class ClientProfileSerializer(serializers, ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ['company_name', 'website']