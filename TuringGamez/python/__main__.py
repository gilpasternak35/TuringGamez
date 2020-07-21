"""from transformers import pipeline, set_seed
import pandas as pd
import requests, sys, webbrowser,xml
import numpy as np
import bs4
import re
import random
from urllib.error import HTTPError"""
import argparse
from argparse import ArgumentParser
from typing import Any, Callable, Dict, List


def main():
    """[summary]

    Returns:
        [type]: [description]
    """
    # Define a dictionary which maps gametypes to their corresponding
    gametype_map = _init_gametype_dict()

    # Will return individual elements
    parser = _init_argparser(gametype_map.keys())

    # Parse the arguments and return
    # TODO: this doesn't quite work yet, but it's getting close
    print(parser.parse_args())
    # TODO: Goal is (I think) mutually exclusive subcommands for song vs. wiki games. Not sure if possible -Jesse


def _init_gametype_dict() -> Dict[str, Callable[..., Any]]:
    """Initializes a mapping from gametpying strings to Callable functions which execute the
       appropriate game. 


    Returns:
        Dict[str, Callable[..., Any]]: The mapping from gametypes string to appropriate game
                                        function.
    """
    mapper = {
        """'madlib-song': songs.madlibs_song_gameplay, # Mad-Lib games
        'madlib-wiki': wiki.madlib_wiki_gameplay,
        'madlib-quote': quotes.madlibs_quotes_gameplay,
        'guess-song': songs.guessText_song_gameplay, # Guessing Games
        'guess-wiki': wiki.guess_original_wiki_gameplay,
        'guess-quote': quotes.guessText_quotes_gameplay"""
        # TODO: ...shouldn't there be more games? I feel like I'm missing some but there only
        #       seemed to be 3 distinct game functions. -Jesse
    }
    # return mapper # TODO: put this real one back, once we fix the project structure (talk to jesse)
    return {'game-1': lambda: print('I\'ll bite your leg off'), 'game-2': lambda: print('hello-world')}


def _init_argparser(game_modes: List[str]) -> ArgumentParser:
    """[summary]

    Returns:
        [type]: [description]
    """
    # Create the program and description
    parser = argparse.ArgumentParser(
        prog='TuringGamez', description='A TuringGamez model')

    # Set game mode
    help_str = 'Valid game types:\n'
    for gt in game_modes:
        help_str += gt + ','
    parser.add_argument('game-type', choices=game_modes, help=help_str)

    # Set game difficulty
    parser.add_argument('--difficulty', '-d',
                        help='Difficulty level: [1-...]', metavar='D')

    # Make Song and Wikipedia arguments mutually exclusive #TODO: more descriptive name for argument group
    non_conflicting_args = parser.add_mutually_exclusive_group()  # TODO: didn't work yet

    """
    Set game-type parameters for 'Song' games
    """  # 'Song Game Required Args:'
    non_conflicting_args.add_argument('--artist', '-a', metavar='ARTIST',
                                      dest='song-game', help='Name of artist for song games')
    song_subparser = parser.add_subparsers(dest='song-game')
    song_subparser.add_parser('title')
    # parser.add_argument('--song-title', '-t', metavar='TITLE',
    #                     help='Title of song for song games')
    """song_parser = parser.add_subparsers(help='Subcommand', dest='artist')
    song_parser.add_parser('-t', #'-t', metavar='TITLE',
                           help='Title of song for song games')"""

    """
    Set game-type parameters for 'Wiki' games
    """  # 'Wikipedia Game Required Args:'
    non_conflicting_args.add_argument('--wiki-topic', '-w', metavar='TOPIC', dest='wiki-game',
                                      help='An initial topic to search on Wikipedia.org for Wikipedia games')
    # parser.add_argument('--wiki-links', '-l', metavar='L',
    #                        help='A number of links to follow on wikipedia in wiki games')
    """
    parser.add_argument('--wiki-topic', '-w', metavar='TOPIC',
                                      help='An initial topic to search on Wikipedia.org for Wikipedia games')
    wiki_parser = parser.add_subparsers(help='Subcommand')
    wiki_parser.add_parser('--wiki-links', '-l', metavar='L',
                                      help='A number of links to follow on wikipedia in wiki games')"""

    return parser


if __name__ == '__main__':
    main()
