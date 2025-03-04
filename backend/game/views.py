from django.shortcuts import render
from rest_framework.views import APIView
from .models import Song
from .serializers import SongSerializer

# Create your views here.
class SongList(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
