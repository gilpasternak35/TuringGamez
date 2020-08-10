import re
from typing import List, Tuple
import bs4
import numpy as np
import requests
from transformers.pipelines import Pipeline


# Runs the madlibs wikipedia version (returns messed up text)
def wiki_gameplay(topic: str, pages: int, level: int, nlp: Pipeline) -> Tuple[str, str, str]:
    """[summary]

    Args:
        topic (str): [description]
        pages (int): [description]
        level (int): [description]
        nlp (Pipeline): [description]

    Returns:
        Tuple[str, str, str]: [description]
    """
    text, title = wiki_search(topic, pages)
    old_text = ' '.join(text)
    # Insurance against text too big for language model
    if(len(text) > 350):
        text = text[:350]
    new_text, indices = replace_words_at_random(nlp, text, level)
    return new_text, old_text, title


# Iterates through wikipedia pages
def wiki_search(topic: str, pages: int) -> Tuple[str, str]: # TODO: double check type of textSoup, was tired -Jesse
    """[summary]

    Args:
        topic (str): [description]
        pages (int): [description]

    Returns:
        Tuple[str, str]: [description]
    """
    textSoup, title = looping_wiki_search(topic, pages)
    return textSoup, title


# Randomly selecting the next topic to be searched for
def select_next_topic(text: List[str]) -> str:
    """[summary]

    Args:
        text (List[str]): [description]

    Returns:
        str: [description]
    """
    random_number = np.random.randint(1, len(text))
    return text[random_number]


# Replaces hyphens with an underscore for url purposes, removes all punctuation that could break url
def replace_punctuation(text: str) -> str:
    """[summary]

    Args:
        text (str): [description]

    Returns:
        str: [description]
    """
    remove_whitespace = text.strip()
    #remove_dashes = remove_whitespace.replace('-', ' ') 
    #remove_dashes = remove_dashes.replace(' ', '_')
    replace_dashes = remove_whitespace.replace('-', '_') # TODO: saved a step from above two lines

    # Remove all non-word characters. Removes punctuation, extraneous symbols, etc (but not '_')
    pattern = re.compile(r'\W')
    remove_symbols = re.sub(pattern, '', replace_dashes)

    return remove_symbols


# Loop through connected topics on wikipedia to find a "landing page", then return the text of that landing page. By default, returns the page of 'topic'
def looping_wiki_search(topic: str, neighbor_pages=0) -> Tuple[str, str]:
    """[summary]

    Args:
        topic (str): [description]
        neighbor_pages (int, optional): [description]. Defaults to 0.

    Returns:
        Tuple[str, str]: [description]
    """
    searchText = ""
    url = construct_wiki_url(topic)
    original = construct_wiki_url(topic)
    for i in np.arange(neighbor_pages + 1):
        print(i)

        # Putting in a try-catch in the case that we have reached a nonexistent page, taking back to original which we
        # Know actually exists
        try:
            searchText = get_wiki_text(url).split(" ")
        except requests.HTTPError:
            searchText = get_wiki_text(original).split(" ")

        # So long as there are still pages left to proccess
        if (i < neighbor_pages):
            # Selecting next topic
            topic = select_next_topic(searchText)

            # Replacing the punctuation of the next topic
            topic = replace_punctuation(topic)

            # Moving to next URL
            url = construct_wiki_url(topic)

    return searchText, topic


# Takes a given user topic and constructs a valid wikipedia url
def construct_wiki_url(url_topic: str) -> str:
    """[summary]

    Args:
        url_topic (str): [description]

    Returns:
        str: [description]
    """
    return ('https://en.wikipedia.org/wiki/' + url_topic.lower().strip().replace(" ", "_"))


# Obtains text from a wikipedia url
def get_wiki_text(url: str) -> str:
    """[summary]

    Args:
        url (str): [description]

    Returns:
        str: [description]
    """
    # Requesting data from url, finding specialized tags for this particular website
    res = requests.get(url)
    res.raise_for_status()

    # Attaching soup object to page text, obtaining text in paragraphs
    soup = bs4.BeautifulSoup(res.text, "lxml")
    text = ""

    # Problematic structure: fails to look for list items which make up substantial amount of wikipedia pages
    for paragraph in soup.find_all('p'):
        text += paragraph.text

    # Formatting the string so that it looks normal
    text = re.sub(r'\[.*\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text
