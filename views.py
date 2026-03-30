from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour
# Create your views here.
from django.http import HttpResponse
from .forms import TourForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import bookingForm
from django.urls import reverse


def tours_show_view(request):
    tours_objects = Tour.objects.all()
    template_name = "tours/tour.html"
    context = {"tours_objects": tours_objects}
    return render(request, template_name, context)


@login_required(login_url="/users/login/")
def add_tours_view(request):
    if request.method == "GET":
        tour_form = TourForm()
        template_name = "tours/add_tours.html"
        context = {"tour_form": tour_form}
        return render(request, template_name, context)
    elif request.method == "POST":
        tour_filled_form = TourForm(request.POST, request.FILES)
        if tour_filled_form.is_valid():
            tour_filled_form.save()
            return redirect("/tours/show/")


@login_required(login_url="/users/login/")
def updatetoursview(request, i):
    tour = Tour.objects.get(id=i)
    if request.method == "GET":
        tour_update_form = TourForm(instance=tour)
        template_name = "tours/add_tours.html"
        context = {"tour_form": tour_update_form}
        return render(request, template_name, context)
    elif request.method == "POST":
        tour_filled_form = TourForm(request.POST, request.FILES, instance=tour)
        if tour_filled_form.is_valid():
            tour_filled_form.save()
            return redirect("/tours/show/")


@login_required(login_url="/users/login/")
def Deletetoursview(request, i):
    tour = Tour.objects.get(id=i)
    tour.delete()
    return redirect("/tours/show/")


def search(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = Tour.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
    return render(request, "tours/search.html", {"query": query, "results": results})


@login_required(login_url="/users/login/")
def bookingview(request):
    # tour = Tour.objects.get(id=i)
    if request.method == "GET":
        tour_book_form = bookingForm()
        # tour_book_form.fields['tour'].empty_label= None
        template_name = "tours/book.html"
        context = {"form": tour_book_form}
        return render(request, template_name, context)
    elif request.method == "POST":
        form = bookingForm(request.POST)
        print("errors", form.errors)
        print("is valid:", form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            form = bookingForm()
        return render(request, "tours/book.html", {"form": form})


def success(request):
    return render(request, "tours/success.html")
