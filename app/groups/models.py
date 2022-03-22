from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owner")
    created_at = models.DateTimeField(auto_now_add=True)
    # members = models.ManyToManyField(CustomUser, related_name="members")
    members = models.ManyToManyField(to=CustomUser)
    # events
    
    def __str__(self):
        return f"{self.name}"