import os
import django
import requests
import re
from bs4 import BeautifulSoup

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Replace with your project name
django.setup()

from game.models import Album, Song  # Replace with your app name

# Wikipedia URL for Eminem's discography
wiki_url = "https://en.wikipedia.org"
artist_url = wiki_url + "/wiki/Eminem_albums_discography"

# Regex for extracting song and feature names
song_regex = r'"(.*?)"'
feature_regex = r'\((?:with|featuring)\s(.*?)(?:\[\w+\])?\)'

# List of albums to include
albums_to_include = [
    "The Slim Shady LP",
    "The Marshall Mathers LP",
    "The Eminem Show",
    "Encore",
    "Relapse",
    "Recovery",
    "The Marshall Mathers LP 2",
    "Revival",
    "Kamikaze",
    "Music to Be Murdered By",
    "The Death of Slim Shady (Coup de Grâce)"
]

def scrape():
    """
    Scrapes Wikipedia to extract Eminem's discography and saves data to the database.
    """
    response = requests.get(artist_url)
    soup = BeautifulSoup(response.content, "html.parser")

    albums_list = soup.find_all(attrs={"scope": "row"})
    album_links = [wiki_url + album.find("a").get("href") for album in albums_list if album.text in albums_to_include]
    album_number = 1
    for album_link in album_links:
        scrape_album_page(album_link, album_number)
        album_number += 1


def scrape_album_page(album_link, album_number):
    """
    Extracts album and song details from the Wikipedia page of an album.
    """
    response = requests.get(album_link)
    soup = BeautifulSoup(response.content, "html.parser")

    album_name = soup.find(class_="firstHeading mw-first-heading").find("i").text
    songs = list(soup.find(class_="tracklist").find("tbody"))[1:-1]

    # Create or get album in the database
    album, _ = Album.objects.get_or_create(name=album_name, album_number=album_number)

    for song in songs:
        save_song_to_db(song, album)


def save_song_to_db(song, album):
    """
    Extracts song details and saves it to the database.
    """
    song_title_text = song.find_next().find_next().text
    track_number = int(song.find_next().text[:-1])
    track_length = song.find_next(class_="tracklist-length").text
    feature_match = re.search(feature_regex, song_title_text)

    song_name = re.search(song_regex, song_title_text).group(1)
    features = feature_match.group(1) if feature_match else None

    # Save song to database
    if '(skit)' not in song_name.lower():
        Song.objects.create(
            song_name=song_name,
            album=album,
            track_number=track_number,
            track_length=track_length,
            features=features
        )

if __name__ == "__main__":
    Song.objects.all().delete()
    scrape()
