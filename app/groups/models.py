from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="group_owner")
    created_at = models.DateTimeField(auto_now_add=True)
    # members = models.ManyToManyField(CustomUser, related_name="members")
    members = models.ManyToManyField(to=CustomUser)
    # fix event representation
    # events = models.ForeignKey(to=Event, related_name="group", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="event_owner")
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=512, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    # attendees = models.ManyToManyField(to=CustomUser)
    attendees = models.ManyToManyField(CustomUser, related_name="events")
    # posts = models.ForeignKey(Posts)
    group = models.ForeignKey(to=Group, related_name="group", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.name}"   