
# Register your models here.

from django.contrib import admin
from .models import Tower, Report, Antenna, StressResult

admin.site.register(Tower)
admin.site.register(Antenna)
admin.site.register(StressResult)
admin.site.register(Report)

