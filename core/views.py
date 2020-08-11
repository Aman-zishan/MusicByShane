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

#error handler

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
