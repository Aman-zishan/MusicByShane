from django.db import models


class Track(models.Model):

    title = models.CharField(max_length=100)

    date = models.DateField(default="--/--/--")
    image = models.ImageField(default="image",upload_to="Tracks/images/")
    audio = models.FileField(default="audio",upload_to="Tracks/audio/")

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(default="program title",max_length=100)
    program_date = models.DateField(default="--/--/--")
    program_location = models.CharField(default="city/place",max_length=100)
    description = models.CharField(default="program description",max_length=200)


    def __str__(self):
        return self.title

class Gallery_image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default="image",upload_to="gallery/")

    def __str__(self):
        return self.title
