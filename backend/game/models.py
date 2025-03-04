from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=255, unique=True)
    album = models.CharField(max_length=255)
    album_number = models.IntegerField()
    track_number = models.IntegerField()
    track_length = models.CharField(max_length=10)
    features = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.song_name
