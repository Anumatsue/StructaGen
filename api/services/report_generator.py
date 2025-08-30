from docxtpl import DocxTemplate
from django.core.files.base import ContentFile
from io import BytesIO
from datetime import datetime


class ReportGenerator:
    def __init__(self, tower, include_stress=True, user=None, template_path="templates/struct_report_template.docx"):
        self.tower = tower
        self.include_stress = include_stress
        self.user = user
        self.template_path = template_path

    def _collect_context(self):
        antennas = list(self.tower.antennas.all().values(
            "antenna_type", "mount_height_m", "length_m", "width_m", "depth_m", "epa", "fpa", "notes"
        ))
        stress = list(self.tower.stress_results.all().values("member_id", "axial_stress", "bending_stress", "notes"))
        ctx = {
            "tower": {
                "name": self.tower.name,
                "location": self.tower.location,
                "height_m": self.tower.height_m,
                "tower_type": self.tower.tower_type,
            },
            "antennas": antennas,
            "stress_results": stress if self.include_stress else [],
            "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
            "generated_by": getattr(self.user, "username", "system"),
        }
        return ctx

    def generate_docx_bytes(self):
        ctx = self._collect_context()
        doc = DocxTemplate(self.template_path)
        doc.render(ctx)
        f = BytesIO()
        doc.save(f)
        f.seek(0)
        return f.read()

    def generate_and_save(self):
        from ..models import Report
        data = self.generate_docx_bytes()
        filename = f"{self.tower.name.replace(' ','_')}_report_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.docx"
        report = Report.objects.create(
            owner=self.user,
            tower=self.tower,
            title=f"{self.tower.name} Structural Report",
        )
        report.docx_file.save(filename, ContentFile(data))
        report.metadata = {"generated_at": datetime.utcnow().isoformat(), "include_stress": self.include_stress}
        report.save()
        return report
