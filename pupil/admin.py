from django.contrib import admin
from .models import Pupil

class PupilAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pupil, PupilAdmin)
