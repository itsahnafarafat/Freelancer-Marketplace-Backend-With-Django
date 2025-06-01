from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class FreelanceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField(blank=True)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
