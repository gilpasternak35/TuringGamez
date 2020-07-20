import lyricsgenius
import re


#Runs the madlibs game, song edition and returns the resulting text (replace words and return funny texts)
def madlibs_song_gameplay(artist_name: str, song_name: str, level: int, nlp) -> str:
    # Some songs are too long, so expect this and auto replace with Africa by Toto
    lyrics = obtain_lyrics(artist_name, song_name)
    # We only need to return modifications
    try:
        text, indices = replace_words_at_random(nlp, lyrics, level)
    except RuntimeError:
        print(len(lyrics))
        lyrics = obtain_lyrics("Toto", "Africa")
        text, indices = replace_words_at_random(nlp, lyrics, level)
    return text.replace("\'", "")


# Runs the madlibs game, song edition and returns the resulting text (replace words and return funny texts)
def guessText_song_gameplay(artist_name: str, song_name: str, level: int, nlp):
    # Some songs are too long, so expect this and auto replace with Africa by Toto
    lyrics = obtain_lyrics(artist_name, song_name)
    ret = " ".join(lyrics)
    # We only need to return modifications
    try:
        text, indices = replace_words_at_random(nlp, lyrics, level)
    except RuntimeError:
        print(len(lyrics))
        lyrics = obtain_lyrics("Toto", "Africa")
        text, indices = replace_words_at_random(nlp, lyrics, level)
    return text.replace("\'", ""), ret


# Takes artist and song name in terms of string and obtains lyrics
def obtain_lyrics(artist: str, song: str) -> [str]:
    genius = lyricsgenius.Genius("NDltUrlbSis8n9o1FEyGUE_ruIlngdDmXwoQdvrkX0hh3le3LKF8XalcHXOetm3x")
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


# Master Controls obtaining and proccessing lyrics
# To do: preserve tags, ie [verse 1], and keep word replacement model from touching it
def lyrics(artistName, songName):
    lyrics = obtain_lyrics(artistName, songName)
    return lyrics
