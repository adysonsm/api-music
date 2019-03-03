from django.db import models

class Track(models.Model):
    track = models.CharField(max_length=200)


    def __str__(self):
        return self.track

