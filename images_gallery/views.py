from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Category, Location


# Create your views here.
def all_images(request):
    location = Location.get_location()
    image = Image.get_images()
    title = "gallery"
    
    return render(request, 'all_images/gallery.html', {"title":title, "image":image,"locations":location})


def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image Category"
        return render(request, 'all_images/search.html',{"message":message})


def filter_by_location(request,location_id):
    
    try:
        location = Location.get_location()
        images_filtered = Image.objects.filter(location = location_id)
    except ValueError:
        raise Http404
        assert False

    return render(request, 'all_images/location.html',{"images":images_filtered, "locations":location})