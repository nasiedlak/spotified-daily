import spotipy
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
    pass
