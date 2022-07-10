from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .forms import *
from .models import *


@login_required(login_url='/')
def history_view(request):
    quotes = Quote.objects.filter(user=request.user).order_by("-date_saved")
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


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    context = {}
    return render(request, "calculator/logout.html", context)


@login_required(login_url='/')
def search_view(request):
    if "search_nav" in request.GET:
        search_nav = request.GET["search_nav"]
        search_dict = {
            "customer__customer_name__icontains": search_nav,
        }
        quote = Quote.objects.filter(**search_dict, user=request.user)
        return render(request, "calculator/search_field.html", {"search_nav": search_nav, "quote": quote})
    else:
        quote = Quote.objects.all()
        return render(request, "calculator/search_field.html", {"quote": quote})


@login_required(login_url='/')
def quote_detail(request, slug=None):
    quote = get_object_or_404(Quote, slug=slug, user=request.user)
    context = {
        "quote": quote
    }
    return render(request, "calculator/quote_detail.html/", context)


@login_required(login_url='/')
def current_offer(request):
    offer = Service.objects.all().order_by("group", "name")
    context = {"offer": offer}
    return render(request, "calculator/price_book.html", context)


@login_required(login_url='/')
def manual_view(request):
    context = {}
    return render(request, "calculator/main.html", context)


@login_required(login_url='/')
def quote_create_view(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.user_id = request.user
            data = form.save()

            return redirect("/quote_item_add/" + data.slug)
        else:
            pass
    else:
        pass

    form = QuoteForm()
    context = {"form": form}
    return render(request, "calculator/quote_create.html", context)


@login_required(login_url='/')
def quote_item_add(request, slug):
    data = Quote.objects.get(slug=slug)
    if request.method == "POST":
        form = QuoteItemForm(request.POST)
        form.quote = data
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        pass

    form = QuoteItemForm()
    context = {"form": form}
    return render(request, "calculator/quoteitem_add.html", context)
