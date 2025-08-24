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

    
    def __str__(self):
        return self.name

def report_upload_path(instance, filename):
    return f"reports/user_{instance.owner.id}/tower_{instance.tower.id}/{filename}"    

class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="reports")
    docx_file = models.FileField(upload_to=report_upload_path)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default="Structural Report")
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Report {self.id} for {self.tower.name}"

