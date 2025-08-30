
from django.conf import settings
from django.db import models
from django.utils import timezone
from .services.report_generator import ReportGenerator

User = settings.AUTH_USER_MODEL

class Tower(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="towers")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)   # will optionally change to PointField later 
    height_m = models.FloatField()
    tower_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.location})"

drag_factor = 1.3
class Antenna(models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="antennas")
    antenna_type = models.CharField(max_length=200)
    mount_height_m = models.FloatField()
    length_m = models.FloatField(null=True, blank=True)
    width_m = models.FloatField(null=True, blank=True)
    depth_m = models.FloatField(null=True, blank=True)
    epa = models.FloatField(null=True, blank=True)   # calculated below
    fpa = models.FloatField(null=True, blank=True)   # calculated below
    notes = models.TextField(blank=True)
    
    def calculate_epa_fpa(self):
        #Certified forular for calculating epa and fpa as per IHS standards
        if self.length_m and self.width_m and self.depth_m:
            self.epa = (self.length_m * self.width_m * drag_factor)
            self.fpa = (self.length_m * self.width_m)

    def save(self, *args, **kwargs):
        # auto-calculate epa and fpa before saving
        self.calculate_epa_fpa()
        super().save(*args, **kwargs)
   
    def __str__(self):
        return f"{self.antenna_type} @ {self.mount_height_m}m"


class StressResult(models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="stress_results")
    member_id = models.CharField(max_length=200)
    max_stress_ratio_legs = models.FloatField()
    max_stress_ratio_bracings = models.FloatField()
    deflection_value_uls = models.FloatField()
    deflection_value_sls = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)


def report_upload_path(instance, filename):
    return f"reports/user_{instance.owner.id}/tower_{instance.tower.id}/{filename}"

class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name="reports")
    docx_file = models.FileField(upload_to=report_upload_path)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default="Structural Report")
    metadata = models.JSONField(default=dict, blank=True)

    

    def save(self, *args, **kwargs):
        # Only auto-generate if docx_file is empty
        if not self.docx_file:
            generator = ReportGenerator(tower=self.tower, user=self.owner)
            docx_bytes = generator.generate_docx_bytes()
            
            filename = f"{self.tower.name.replace(' ', '_')}_report_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.docx"
            self.docx_file.save(filename, ContentFile(docx_bytes), save=False)

            #metadata
            self.metadata = {
                "generated_at": datetime.utcnow().isoformat(),
                "include_stress": generator.include_stress,
            }

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Report {self.id} for {self.tower.name}"

