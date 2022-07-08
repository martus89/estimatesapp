from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
def manual_view(request):

    quote = QuoteForm(request.POST)
    formset = QuoteItemFormSet(request.POST)

    if request.method == "POST":
        if formset.is_valid() and quote.is_valid():
            quote.save()
            formset.instance = quote
            formset.save()
            return redirect("/history")

    context = {"formset": formset, "quote": quote}
    return render(request, "calculator/manual.html", context)

    # if request.method == "POST":
    #     quoteform = QuoteForm(request.POST)
    #     itemform = QuoteItem(request.POST)
    #
    #     if quoteform.is_valid() and itemform.is_valid():
    #         quoteform.save()
    #         itemform.save()
    #         context = {"quoteform": quoteform, "itemform": itemform}
    #     else:
    #         pass
    #
    # else:
    #     pass


# not working
@login_required(login_url='/')
def search_view(request):
    if request.method == ["GET"]:
        search = request.GET["search"]
        quotes = Quote.objects.filter(customer__quote__comment__startswith=search)
        context = {"search": search, "quotes": quotes}
        return render(request, "calculator/search_field.html", context)
    else:
        pass
        context = {}
    return render(request, "calculator/search_field.html", context)


@login_required(login_url='/')
def quote_detail(request):
    context = {}
    return render(request, "calculator/quote_detail.html", context)


@login_required(login_url='/')
def current_offer(request):
    offer = Service.objects.all().order_by("group", "name")
    context = {"offer": offer}
    return render(request, "calculator/current_offer.html", context)
