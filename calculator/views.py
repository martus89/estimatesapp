from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def history_view(request):
    if request.user.is_authenticated:
        quotes = Quote.objects.all()
    else:
        response = redirect('/')
        return response
    context = {"quotes": quotes}
    return render(request, "calculator/history.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('/manual/')
            return response
        else:
            messages.success(request, "You sure these credentials are valid? Try again.")
            return redirect("/")
    else:
        return render(request, "calculator/login.html", {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        pass
    else:
        response = redirect('/')
        return response
    context = {}
    return render(request, "calculator/logout.html", context)


def manual_view(request):
    if request.user.is_authenticated:
        pass
    else:
        response = redirect('/')
        return response
    context = {}
    return render(request, "calculator/manual.html", context)
