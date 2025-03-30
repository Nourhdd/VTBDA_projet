from django.contrib import admin
from .models import Patient, Doctor, Appointment, Hospital, Profile

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Hospital)
admin.site.register(Profile)
