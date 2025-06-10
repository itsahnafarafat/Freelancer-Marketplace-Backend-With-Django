from rest_framework import serializers
from .models import JobPost, Application
from django.contrib.auth import get_user_model

User = get_user_model()

class JobPostSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = JobPost
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    freelancer = serializers.StringRelatedField(read_only=True)
    job = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = '__all__'

