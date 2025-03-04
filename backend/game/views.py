from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song, GameSession
from .serializers import SongSerializer
from .game_logic import process_guess
import random, re


@api_view(['POST'])
def start_game(request):
    """Starts a new game by selecting a random song."""
    song = random.choice(Song.objects.all())
    game = GameSession.objects.create(correct_song=song, guesses_left=10)

    return Response({
        'game_id': game.id,
        'guesses_left': game.guesses_left
    })


@api_view(['POST'])
def check_guess(request):
    """API view to check user's guess."""
    game_id = request.data.get("game_id")
    user_guess = request.data.get("guess")

    game = get_object_or_404(GameSession, id=game_id)
    correct_song = game.correct_song

    if game.guesses_left <= 0:
        return Response({
            'message': 'Game over!',
            'correct_song': {
                'song_name': game.correct_song.song_name,
                'album': game.correct_song.album.name,
                'track_number': game.correct_song.track_number,
                'track_length': game.correct_song.track_length,
                'features': game.correct_song.features
            }
        })
    
    is_correct = user_guess.lower() == correct_song.song_name.lower()

    guessed_song = Song.objects.filter(song_name__iexact=user_guess).first()
    if not guessed_song:
        return Response({
            'message': 'Song not found',
            'guesses_left': game.guesses_left
        })
    
    response_data = process_guess(correct_song, guessed_song)

    game.guesses_left -= 1
    game.save()

    return Response({
        'guesses_left': game.guesses_left,
        'won': is_correct,
        'guess': response_data
    })

