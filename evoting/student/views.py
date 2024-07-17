from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == "POST":
        # Get the form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        print(username,password)

        # Check if the username or email is already taken
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return HttpResponse("Username or email already taken")
        user = User.objects.create(username=username,
                                   email=email,
                                   )
        user.set_password(password)                           
        print(username,password)                           
        user.save()

        return HttpResponse("Account created successfully")

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username = username).exists():
                messages.error(request,'Invalid Username')  
            user = authenticate(username =username,password=password)
            if user is None:
                messages.error(request,'Incorrect Password')
                return redirect('login')
            else:
                login(request,user) 
                return render(request,'dashboard.html')

    return render(request,'login.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if not User.objects.filter(username=username).exists():
#             messages.error(request, 'Invalid Username')
#         elif user is None:
#             messages.error(request, 'Incorrect Password')
#         else:
#             print("Login successful. Redirecting to dashboard.")
#             login(request, user)
#             return redirect('dashboard')

#     return render(request, 'login.html')

def dashboard(request):
    return render(request,'dashboard.html')