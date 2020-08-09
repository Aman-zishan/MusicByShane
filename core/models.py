from django.db import models


class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField(default="--/--/--")
    '''

    description = models.TextField()
    '''

    image = models.ImageField(default="image")
    audio = models.FileField(default="audio")

    def __str__(self):
        return self.title
