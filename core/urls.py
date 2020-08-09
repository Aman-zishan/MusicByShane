from django.urls import path, re_path
from .views import home, tracks, about

app_name = "core"


urlpatterns = [

    path('', home, name="home"),
    path('tracks', tracks, name="tracks"),
    path('about', about, name="about"),



]
