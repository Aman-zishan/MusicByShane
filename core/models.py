from django.db import models


class Track(models.Model):

    title = models.CharField(max_length=100)

    date = models.DateField(default="--/--/--")
    image = models.ImageField(default="image")
    audio = models.FileField(default="audio")

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.TextField(default="program title")
    prg_date = models.DateField(default="--/--/--")


    def __str__(self):
        return self.title
