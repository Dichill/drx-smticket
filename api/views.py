from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import *
from .scraper import *
import json


# Create your views here.
def home(request):
    EventResult.objects.all().delete()
    # Fetch the Events
    FetchEvents()

    events = EventResult.objects.all()
    context = {'events':events}

    return render(request, "index.html", context)

def search(request):
    MovieResult.objects.all().delete()
    q = request.GET.get('q')
    template_name = "search.html"

    # Lets Fetch the Results
    FetchMovieResults(q)

    # After fetching we want to bring it to the Front-End
    #print(movies.filter(location='Mall Of Asia Arena'))
    movies = MovieResult.objects.all()
    context = {'movies':movies}
    
    return render(request, template_name, context)
    
    
def custom_page_not_found_view(request, exception):
    return render(request, "error.html", {})

def custom_error_view(request, exception=None):
    return render(request, "error.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "error.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "error.html", {})