"""from transformers import pipeline, set_seed
import pandas as pd
import requests, sys, webbrowser,xml
import numpy as np
import bs4
import re
import random
from urllib.error import HTTPError"""
import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, Callable, Dict, Optional, Sequence, Text, Union, Iterable, Tuple
from TuringGamez.python import quotes, songs, wiki


def main():
    '''[summary]

    Returns:
        [type]: [description]
    '''
    # Define a dictionary which maps gametypes to their corresponding
    song_dict, wiki_dict, quote_dict = _init_gametype_dict()

    # Will return individual elements
    parser = _init_argparser(song_dict.keys(), wiki_dict.keys(), quote_dict.keys(),
                             range(1, 4))  # TODO: Verify the difficulty range

    # Join all game maps into a single map
    game_function_map = {**song_dict, **wiki_dict, **quote_dict}

    # Parse the arguments and return
    # TODO: this doesn't quite work yet, but it's getting close
    # parser.print_help()
    # print(parser.parse_args(['--difficulty', '2', 'song', '--title', 'title', '--artist', 'artist', '--type', 'type']))
    # print(parser.parse_args(['wiki', '--topic', 'topic', '--number-of-links', '3', '--type', 'type']))
    # print(parser.parse_args(['song', '-h']))
    # print(parser.parse_args(['wiki', '-h']))
    print(parser.parse_args(['quote', '-h']))


def _init_gametype_dict() -> Tuple[Dict[str, Callable[..., Any]],
                                   Dict[str, Callable[..., Any]],
                                   Dict[str, Callable[..., Any]]]:
    """Initializes a mapping from gametpying strings to Callable functions which execute the
       appropriate game. 


    Returns:
        Dict[str, Callable[..., Any]]: The mapping from gametypes string to appropriate game
                                        function.
    """
    song_map = {
        'madlib-song': songs.madlibs_song_gameplay,  # Song games
        'guess-song': songs.guessText_song_gameplay
    }
    wiki_map = {
        'guess-wiki': wiki.wiki_gameplay,  # Wiki Games
        'madlib-wiki': wiki.wiki_gameplay
    }
    quote_map = {
        'madlib-quote': quotes.madlibs_quotes_gameplay,  # Quote Games
        'guess-quote': quotes.guessText_quotes_gameplay
        # TODO: Noticed 8/8/2020 both quote functions are, line for line, *identical*. Should be combined.
        # TODO: ...shouldn't there be more games? I feel like I'm missing some but there only
        #       seemed to be 3 distinct game functions. -Jesse ***As of 8/8/2020 I'm still not sure I have all games
    }
    return song_map, wiki_map, quote_map


def _init_argparser(song_choices: Iterable[str], wiki_choices: Iterable[str],
                    quote_choices: Iterable[str], difficulty_levels: range) -> ArgumentParser:
    """[summary]

    Returns:
        [type]: [description]
    """
    # Create the overall program parser
    parser = argparse.ArgumentParser(prog='TuringGamez', description='A TuringGamez model')

    # Parent parser
    # Defines common arguments between game types: --difficulty, --type
    parent_parser = argparse.ArgumentParser(add_help=False)
    # Sets game difficulty
    parent_parser.add_argument('--difficulty', '-d', type=int, default=2, choices=difficulty_levels,
                               help=f'Difficulty level: [{difficulty_levels.start} - {difficulty_levels.stop - 1}]',
                               metavar='D')
    # parent_parser.add_argument('--type', dest='type',type=str, action='store', help='This is a default help message.')
    # TODO: Goal - add the type argument to the parent, override choices for each sub-parser. (Compiler error?)

    # Game modes are made mutually exclusive using sub-command parsers (i.e. 'git commit' and 'git push' are
    # mutually exclusive commands)
    # Command Structure: (any new game types would be added as additional sub-commands)
    # prog.py  --difficulty D --help
    #         song _artist_ _title_
    #         wiki _topic_ _#-links_
    #         quote
    #         ...

    # Create subparsers
    subparsers = parser.add_subparsers(dest='game-type')
    subparsers.required = True  # This forces users to provide a game type

    # Create 'song' sub-parser
    song_parser = subparsers.add_parser('song', description='Parse song game arguments', parents=[parent_parser])
    song_parser.add_argument('--artist', type=str, action='store',
                             help='Name of artist for song games')  # metavar='A', possible to default 'ARTIST'
    song_parser.add_argument('--title', type=str, action='store',
                             help='Title of song for song games')  # metavar='T', possible to default 'TITLE'
    # Enables more specificity w/in song games
    song_parser.add_argument('--type', type=str, action='store', choices=song_choices, default=list(song_choices)[0],
                             help='The name of the specific song game to play')

    # Create 'wiki' sub-parser
    wiki_parser = subparsers.add_parser('wiki', description='Parse wiki game arguments', parents=[parent_parser])
    wiki_parser.add_argument('--topic', type=str, action='store',  # metavar='A', possible to default 'ARTIST'
                             help='An initial topic to search on Wikipedia.org for Wikipedia games')
    wiki_parser.add_argument('--number-of-links', metavar='N', type=int, action='store', choices=range(0, 100),
                             help='A number of links to follow on Wikipedia in wiki games')
    # Enables more specificity w/in wiki games
    wiki_parser.add_argument('--type', type=str, action='store', choices=wiki_choices, default=list(wiki_choices)[0],
                             help='The name of the specific wiki game mode to play')

    # Create 'quote' sub-parser
    # Quote games have no arguments, so this acts as a flag
    quote_parser = subparsers.add_parser('quote', description='Parse quote game arguments', parents=[parent_parser])
    # Enables more specificity w/in quote games
    quote_parser.add_argument('--type', type=str, action='store', choices=quote_choices, default=list(quote_choices)[0])

    # Set game mode # TODO: Should not be needed anymore, kept solely as a reminder of how to print all valid game types
    # help_str = 'Valid game types:\n'
    # for gt in game_modes:
    #     help_str += gt + ','
    # parser.add_argument('game-type', choices=game_modes,
    #                     action='store', help=help_str)

    # """ # TODO: No longer needed. Kept only to steal descriptions, docs.
    # Set game-type parameters for 'Song' games
    # """  # 'Song Game Required Args:'
    # non_conflicting_args.add_argument('--artist', metavar='ARTIST',dest='song-game' )
    # song_subparser = parser.add_subparsers(dest='song-game')
    # song_subparser.add_parser('title')
    # # parser.add_argument('--song-title', '-t', metavar='TITLE',)
    #
    # """
    # Set game-type parameters for 'Wiki' games
    # """  # 'Wikipedia Game Required Args:'
    # non_conflicting_args.add_argument('--wiki-topic', '-w', metavar='TOPIC', dest='wiki-game',)
    # # parser.add_argument('--wiki-links', '-l', metavar='L',)

    return parser


if __name__ == '__main__':
    main()
