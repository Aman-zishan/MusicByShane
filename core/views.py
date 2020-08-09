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
'''
def download(request, id):
    obj = Track.objects.get(id=id)
    filename = obj.audio.path
    response = FileResponse(open(filename, 'rb'))
    return response
'''
