"""apismticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path
from api import views

handler404 = 'api.views.custom_page_not_found_view'
handler500 = 'api.views.custom_error_view'
handler403 = 'api.views.custom_permission_denied_view'
handler400 = 'api.views.custom_bad_request_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('documentation/', views.documentation, name="documentation"),
    path('results/', views.search, name="results"),

    # API
    path('api/', views.documentation, name="documentation"),
    path('api/sm_venues', views.SMVenues.as_view(), name="API_SMVENUES"), # SM Venues
    path('api/sm_events', views.SMEvent.as_view(), name="API_SMEVENTS"), # SM Events
    path('api/sm_othervenues', views.OtherVenues.as_view(), name="API_SMOTHERVENUES"), # SM Other Venues
    path('api/sm_attractions', views.Attractions.as_view(), name="API_ATTRACTIONS"), # SM Attractions

    # Automation
    path('login/', views.login, name="login"),
    path('automate/', views.automate, name="automate")
]

