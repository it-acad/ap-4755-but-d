# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authentication.models import CustomUser

def home_view(request):
    if request.user.is_authenticated:
        return redirect('auth:dashboard')

    return render(request, 'authentication/home.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('auth:dashboard')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        if not first_name or not middle_name or not last_name or not email or not password or not role:
            messages.error(request, 'All fields are required')
            return render(request, 'authentication/register.html')
        
        if CustomUser.get_by_email(email=email) is not None:
            messages.error(request, 'This email is already in use')
            return render(request, 'authentication/register.html')
        user = CustomUser.create(
            email=email,
            password=password,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )
        
        if user is None:
            messages.error(request, "Invalid data")
            return redirect('auth:register')
        if role not in ('0', '1'):
            messages.error(request, "Choose between visitor and admin")
            return redirect('auth:register')
        user.role = int(role)
        user.save()
        
        login(request, user)
        return redirect('auth:dashboard')
        
    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('auth:dashboard')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('auth:login')
        
    return render(request, 'authentication/login.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    context = {
        'role': request.user.role
    }
    return render(request, 'authentication/dashboard.html', context)
    
def logout_view(request):
    # if request.user
    logout(request)
    return redirect('auth:home')
