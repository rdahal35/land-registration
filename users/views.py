from django.contrib.auth import login as dj_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages

from users.models import User
from .forms import UserForm


def home(request):
    context = {
        "link": "home"
    }
    if not request.user.is_anonymous:
        if request.user.is_superuser:
            return redirect("dashboard")
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.pop('username')
            raw_password = form.cleaned_data.pop('password1')
            public_address = form.cleaned_data.pop("public_address")
            print(public_address)
            user = User.objects.filter(public_address=public_address)
            if user:
                messages.error(request, 'Metamask account user already exists')
                print(public_address)
            else:
                if public_address == None:
                    messages.error(
                        request, 'Please login to you Metamask account')
                    print(public_address)
                    return render(request, 'signup.html', {'form': form, "link": 'signup'})
                user = User.objects.create_user(
                    username=username, password=raw_password, public_address=public_address)
                user = authenticate(username=username, password=raw_password)
                dj_login(request, user)
                if user.is_superuser:
                    return redirect('dashboard')
                return redirect('home')

    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form, "link": 'signup'})


# def set_public_address(request):
#     return JsonResponse({"key": "value"})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            dj_login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            elif user.is_active:
                return redirect('home')
        messages.error(request, 'Invalid Username or Password')
    return render(request, "login.html", {"link": "login"})
