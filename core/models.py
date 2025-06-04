from django.db import models
from django.contrib.auth.models import User

    
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    project_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        permissions = [
            ("access_client_dashboard", "Can access clien dashboard")
        ]
    
class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.PositiveIntegerField() # in years

    def __str__(self):
        return self.user.username
    
    class Meta:
        permissions = [
            ("access_freelancer_dashboard", "Can access freelancer dashboard"),
        ]
