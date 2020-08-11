from django.shortcuts import render
from .models import Track, Event, Gallery_image


def home(request):

    length = len(Track.objects.all())
    n = abs(length-4)

    context = {
        "tracks": Track.objects.all()[n:],
        "track_home": Track.objects.all().last(),
        "events": Event.objects.all(),
        "gallery_images": Gallery_image.objects.all(),

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
