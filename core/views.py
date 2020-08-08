from django.shortcuts import render
from .models import Track


def home(request):
    context = {

    }
    return render(request, "home.html")


def tracks(request):

    context = {
        "tracks": Track.objects.all()}

    return render(request, "tracks.html", context)
