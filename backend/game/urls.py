from django.urls import path
from .views import start_game, check_guess, song_suggestions

urlpatterns = [
    path("start-game/", start_game, name="start-game"),
    path("check-guess/", check_guess, name="check-guess"),
    path("suggest-songs/", song_suggestions, name="suggest-songs"),
]
