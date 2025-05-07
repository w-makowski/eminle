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

    guessed_song = Song.objects.filter(song_name__iexact=user_guess).first()
    if not guessed_song:
        return Response({
            'message': 'Song not found',
            'guesses_left': game.guesses_left
        })
    
    is_correct = user_guess.lower() == correct_song.song_name.lower()
    
    response_data = process_guess(correct_song, guessed_song)

    game.guesses_left -= 1
    game.save()

    if game.guesses_left <= 0:
        return Response({
            'message': 'Game over!',
            'guesses_left': game.guesses_left,
            'correct_song': {
                'song_name': correct_song.song_name,
                'album': correct_song.album.name,
                'track_number': correct_song.track_number,
                'track_length': correct_song.track_length,
                'features': correct_song.features
            },
            'hints': {
                'album_hint': response_data['album']['hint'],
                'album_color': response_data['album']['color'],
                'track_number_hint': response_data['track_number']['hint'],
                'track__number_color': response_data['track_number']['color'],
                'track_length_hint': response_data['track_length']['hint'],
                'track_length_color': response_data['track_length']['color'],
                'features_hint': response_data['features']['color'],
                'features_color': response_data['features']['color']
            }
        })

    return Response({
        'guesses_left': game.guesses_left,
        'won': is_correct,
        'guess': response_data
    })

@api_view(['GET'])
def song_suggestions(request):
    """Returns list of up to 5 songs matching partial input."""
    query = request.GET.get("q", "")
    if not query:
        return Response([])

    matches = Song.objects.filter(song_name__icontains=query)[:5]
    suggestions = [{"id": song.id, "name": song.song_name} for song in matches]
    return Response(suggestions)
