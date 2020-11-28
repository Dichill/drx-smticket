from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import *
from .scraper import *
import json

from .serializers import SMVenuesSerializer
from .serializers import EventSerializer
from .serializers import OtherVenueSerializer
from .serializers import AttractionsSerializer


# Create your views here.
def home(request):
    SMVenuesResult.objects.all().delete()
    EventResult.objects.all().delete()
    OtherVenuesResult.objects.all().delete()
    AttractionsResult.objects.all().delete()

    # Fetch the Results
    FetchContainers()

    sm_venues = SMVenuesResult.objects.all()
    other_venues = OtherVenuesResult.objects.all()
    events = EventResult.objects.all()
    attractions = AttractionsResult.objects.all()
    context = {'events':events, 'smvenues':sm_venues, 'othervenues':other_venues, 'attractions':attractions}

    return render(request, "index.html", context)

def search(request):
    MovieResult.objects.all().delete()

    q = request.GET.get('q')
    location = request.GET.get('location')
    print(location)
    template_name = "search.html"

    # Lets Fetch the Results
    FetchMovieResults(q)

    # After fetching we want to bring it to the Front-End
    #print(movies.filter(location='Mall Of Asia Arena'))
    
    movies = MovieResult.objects.all()
    context = {'movies':movies}
    
    return render(request, template_name, context)

def documentation(request):
    return render(request, "")

def login(request):
    return render(request, "sm_login.html")

def automate(request):
    user = request.GET.get('user')
    passw = request.GET.get('pwd')

    return render(request, "automate.html")

class SMVenues(APIView):
    def get(self, request):
        SMVenuesResult.objects.all().delete()

        # Fetch the Results
        FetchContainers()

        sm_venues = SMVenuesResult.objects.all()
        serializer = SMVenuesSerializer(sm_venues, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class SMEvent(APIView):
    def get(self, request):
        EventResult.objects.all().delete()

        # Fetch the Results
        FetchContainers()

        sm_events = EventResult.objects.all()
        serializer = EventSerializer(sm_events, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class OtherVenues(APIView):
    def get(self, request):
        OtherVenuesResult.objects.all().delete()

        # Fetch the Results
        FetchContainers()

        sm_othervenues = OtherVenuesResult.objects.all()
        serializer = OtherVenueSerializer(sm_othervenues, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Attractions(APIView):
    def get(self, request):
        AttractionsResult.objects.all().delete()

        # Fetch the Results
        FetchContainers()

        sm_attractions = AttractionsResult.objects.all()
        serializer = AttractionsSerializer(sm_attractions, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def custom_page_not_found_view(request, exception):
    return render(request, "error.html", {})

def custom_error_view(request, exception=None):
    return render(request, "error.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "error.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "error.html", {})