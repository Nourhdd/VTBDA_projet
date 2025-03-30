import random
import string
import hashlib
from django.contrib.auth.models import User
from django.db import models

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medical_history = models.TextField(blank=True)
    ibe_private_key_hash = models.CharField(max_length=128, blank=True)  # Stocke le hash de la clé

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.ibe_private_key_hash:  
            private_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
            self.ibe_private_key_hash = hashlib.sha256(private_key.encode()).hexdigest()
        super().save(*args, **kwargs)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'En attente'), ('confirmed', 'Confirmé'), ('cancelled', 'Annulé')],
        default='pending'
    )

    def __str__(self):
        return f"RDV {self.id} - {self.patient.user.username} avec {self.doctor.user.username}"
