from django.db import models


# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=255, unique=True)
    album_number = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    song_name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    track_number = models.IntegerField()
    track_length = models.CharField(max_length=10)
    features = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.song_name} ({self.album.name})"
    

class GameSession(models.Model):
    correct_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    guesses_left = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
