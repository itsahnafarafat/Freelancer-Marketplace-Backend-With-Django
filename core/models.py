from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class FreelancerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s profile"
