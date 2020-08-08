import re
from typing import List
import lyricsgenius
from transformers.pipelines import Pipeline


#Runs the madlibs game, song edition and returns the resulting text (replace words and return funny texts)
def madlibs_song_gameplay(artist_name: str, song_name: str, level: int, nlp: Pipeline) -> str:
    """[summary]

    Args:
        artist_name (str): [description]
        song_name (str): [description]
        level (int): [description]
        nlp (Pipeline): [description]

    Returns:
        str: [description]
    """
    # Some songs are too long, so expect this and auto replace with Africa by Toto
    lyrics = _obtain_lyrics(artist_name, song_name)
    # We only need to return modifications
    try:
        text, indices = replace_words_at_random(nlp, lyrics, level)
    except RuntimeError:
        print(len(lyrics))
        lyrics = _obtain_lyrics("Toto", "Africa")
        text, indices = replace_words_at_random(nlp, lyrics, level)
    return text.replace("\'", "")


# Runs the madlibs game, song edition and returns the resulting text (replace words and return funny texts)
def guessText_song_gameplay(artist_name: str, song_name: str, level: int, nlp: Pipeline):
    """[summary]

    Args:
        artist_name (str): [description]
        song_name (str): [description]
        level (int): [description]
        nlp (Pipeline): [description]

    Returns:
        [type]: [description]
    """
    # Some songs are too long, so expect this and auto replace with Africa by Toto
    lyrics = _obtain_lyrics(artist_name, song_name)
    ret = " ".join(lyrics)
    # We only need to return modifications
    try:
        text, indices = replace_words_at_random(nlp, lyrics, level)
    except RuntimeError:
        print(len(lyrics))
        lyrics = _obtain_lyrics("Toto", "Africa")
        text, indices = replace_words_at_random(nlp, lyrics, level)
    return text.replace("\'", ""), ret

# Master Controls obtaining and proccessing lyrics
# TODO: preserve tags, ie [verse 1], and keep word replacement model from touching it
def _lyrics(artistName: str, songName: str) -> List[str]:
    """[summary]

    Args:
        artistName (str): [description]
        songName (str): [description]

    Returns:
        List[str]: [description]
    """
    return _obtain_lyrics(artistName, songName)

# Takes artist and song name in terms of string and obtains lyrics
def _obtain_lyrics(artist: str, song: str) -> List[str]:
    """[summary]

    Args:
        artist (str): [description]
        song (str): [description]

    Returns:
        List[str]: [description]
    """
    _GENIUS_KEY = 'NDltUrlbSis8n9o1FEyGUE_ruIlngdDmXwoQdvrkX0hh3le3LKF8XalcHXOetm3x'
    genius = lyricsgenius.Genius(_GENIUS_KEY)
    artist = genius.search_artist(artist, max_songs=3, sort="title")
    song = genius.search_song(song, artist.name)
    song_lyrics = song.lyrics

    # String proccessing 
    song_lyrics = re.sub(r'\[.*\]', '', song_lyrics)
    song_lyrics = re.sub(r'\n+', ' ', song_lyrics)
    song_lyrics = song_lyrics.split(" ")

    # Making sure songs do not exceed maximum threshold
    if (len(song_lyrics) > 510):
        song_lyrics = song_lyrics[:350]
    return song_lyrics
