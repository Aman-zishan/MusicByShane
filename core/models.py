from django.db import models


class Track(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(default="song")
    date = models.DateField(default="--/--/--")
    image = models.ImageField(default="image")
    audio = models.FileField(default="audio")

    def __str__(self):
        return self.title
