from django.urls import path, re_path
from .views import home, tracks, handler404, handler500

app_name = "core"


urlpatterns = [

    path('', home, name="home"),
    path('tracks', tracks, name="tracks"),




]
handler404 = handler404
handler500 = handler500
