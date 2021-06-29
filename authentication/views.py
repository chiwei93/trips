from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, 'User registered successfully. Please login now.')
                return redirect(reverse('login'))
            except:
                messages.error(
                    request, 'User registration failed. Please try again.')
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {
        "form": form,
        "current_page": "register"
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                next = request.GET.get('next')

                if next is None:
                    next = reverse('tours')
                
                return redirect(next)

            else:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'authentication/login.html', {
                    "form": form,
                    "current_page": "login"
                })
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {
        "form": form,
        "current_page": "login"
    })


def logout_user(request):
    logout(request)
    return redirect(reverse('home'))
