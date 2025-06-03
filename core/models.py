from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username
    
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class FreelancerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s profile"
