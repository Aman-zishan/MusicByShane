from django.shortcuts import render
from .models import Track, Event


def home(request):

    context = {
        "tracks": Track.objects.all()[2:],
        "track_home": Track.objects.all().last(),
        "events": Event.objects.all(),

        }

    return render(request, "home.html", context)


def tracks(request):

    context = {
        "tracks": Track.objects.all(),
        "events": Event.objects.all(),
        }

    return render(request, "tracks.html", context)
