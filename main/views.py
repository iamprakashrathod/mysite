from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Tutorial 
from django.contrib import messages

def homepage(request):
    tutorials = Tutorial.objects.all()  # Assuming Tutorial is your model
    return render(request, "main/home.html", {"tutorials": tutorials})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are logged in as {username}")
            return redirect("main:homepage")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            # You can also pass form.errors to the template to display errors

    else:
        form = UserCreationForm()

    return render(request, "main/register.html", {"form": form})
