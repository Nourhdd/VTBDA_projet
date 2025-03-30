from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import PatientRegisterForm, DoctorRegisterForm
from .models import Patient, Doctor
from .ibe_utils import generate_ibe_keys

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            hashed_key, _ = generate_ibe_keys(user.email)
            patient = Patient.objects.create(user=user, ibe_private_key_hash=hashed_key)
            return redirect('login')
    else:
        form = PatientRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
