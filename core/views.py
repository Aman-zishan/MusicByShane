from django.shortcuts import render
from .models import Track


def home(request):

    context = {
        "tracks": Track.objects.all()[2:],
        "track_home": Track.objects.all().reverse()[0],

        }

    return render(request, "home.html", context)


def tracks(request):

    context = {
        "tracks": Track.objects.all()}

    return render(request, "tracks.html", context)
'''
def download(request, id):
    obj = Track.objects.get(id=id)
    filename = obj.audio.path
    response = FileResponse(open(filename, 'rb'))
    return response
'''
