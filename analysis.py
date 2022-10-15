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

    """
    TODO
    
    Run some analysis on listening history and playlists
    combine analysis with user preferences from MongoDB and other factors
    such as time of year and popularity to recommend a song
    """

    uri = ""

    return uri
