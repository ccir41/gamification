from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignInForm, SignUpForm


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                messages.success(request, "User Registered Successfully!")
                return redirect('core:home')
            else:
                messages.success(request, "Something went wrong, please try again later!")
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In!")
                return redirect('core:home')
            else:
                messages.error(request, "Invalid Username or Password!")
        else:
            messages.error(request, "Invalid Username or Password!")
    else:
        form = SignInForm()
    return render(request, 'user/login.html', {'form': form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "User Logged Out!")
    return redirect('user:login')
