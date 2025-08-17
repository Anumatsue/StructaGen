from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class Tower(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="towers")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)   # optionally change to PointField later
    height_m = models.FloatField()
    tower_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
