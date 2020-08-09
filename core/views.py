from django.shortcuts import render
from .models import Track


def home(request):

    context = {
        "tracks": Track.objects.all()[2:],
        "track_home": Track.objects.all().last(),

        }

    return render(request, "home.html", context)


def tracks(request):

    context = {
        "tracks": Track.objects.all()}

    return render(request, "tracks.html", context)



def about(request):
     return render(request, "about.html")
