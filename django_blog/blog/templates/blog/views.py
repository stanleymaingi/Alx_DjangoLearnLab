from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

# Registration view
def register_view(request):
    if request.method == "POST":  # explicit POST
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # explicit save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":  # explicit POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")

# Profile view
@login_required
def profile_view(request):
    if request.method == "POST":  # explicit POST
        email = request.POST.get("email")
        if email:
            request.user.email = email
            request.user.save()  # explicit save()
            messages.success(request, "Profile updated successfully!")
    return render(request, "blog/profile.html", {"user": request.user})