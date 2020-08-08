from django.urls import path
from .views import home, tracks

app_name = "core"


urlpatterns = [

    path('', home, name="home"),
    path('tracks', tracks, name="tracks"),


]