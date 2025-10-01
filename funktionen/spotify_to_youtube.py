import asyncio
from youtubesearchpython import VideosSearch
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

async def spotify_to_youtube(spotify_url: str) -> str:
    """Wandelt einen Spotify-Track-Link in einen YouTube-Link um."""
    try:
        track_id = spotify_url.split("/track/")[1].split("?")[0]
    except IndexError:
        return None

    try:
        track = sp.track(track_id)
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        search_query = f"{artist_name} - {track_name}"
    except Exception as e:
        print(f"Spotify API Fehler: {e}")
        return None

    try:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, lambda: VideosSearch(search_query, limit=1).result())
        if len(result['result']) == 0:
            return None
        return result['result'][0]['link']
    except Exception as e:
        print(f"YouTube-seach issue: {e}")
        return None
