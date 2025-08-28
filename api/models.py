# Create your models here.

# api/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Tower(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="towers")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)   # optionally change to PointField later
    height_m = models.FloatField()
    tower_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

<<<<<<< HEAD
    def __str__(self):
        return f"{self.name} ({self.location})"


class Antenna(models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="antennas")
    antenna_type = models.CharField(max_length=200)
    mount_height_m = models.FloatField()
    length_m = models.FloatField(null=True, blank=True)
    width_m = models.FloatField(null=True, blank=True)
    depth_m = models.FloatField(null=True, blank=True)
    epa = models.FloatField(null=True, blank=True)   # calculated
    fpa = models.FloatField(null=True, blank=True)   # calculated
    notes = models.TextField(blank=True)

    def calculate_epa_fpa(self):
        # placeholder formula. Replace with certified formula later:
        if self.length_m and self.width_m and self.depth_m:
            self.epa = (self.length_m * self.width_m) / max(self.depth_m, 1e-6)
            self.fpa = (self.length_m + self.width_m) / max(self.depth_m, 1e-6)


class StressResult(models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="stress_results")
    member_id = models.CharField(max_length=200)
    axial_stress = models.FloatField()
    bending_stress = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)


def report_upload_path(instance, filename):
    return f"reports/user_{instance.owner.id}/tower_{instance.tower.id}/{filename}"
=======
    
    def __str__(self):
        return self.name

def report_upload_path(instance, filename):
    return f"reports/user_{instance.owner.id}/tower_{instance.tower.id}/{filename}"    
>>>>>>> feature/reports-api

class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="reports")
    docx_file = models.FileField(upload_to=report_upload_path)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default="Structural Report")
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Report {self.id} for {self.tower.name}"

