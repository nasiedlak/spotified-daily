from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from pymongo import MongoClient

import pandas as pd

from sklearn import linear_model, cluster

def analysis(username: str, password: str) -> str:
    """
    Generates a Song of the Day for a given user.

    Returns:
    str: uri of the song

    """
    spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())

    # TODO run some analysis on listening history and playlists

    uri = ""  # TODO combine analysis with user preferences from MongoDB and other factors to recommend a song

    return uri
