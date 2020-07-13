from transformers import pipeline, set_seed
import pandas as pd
import requests, sys, webbrowser,xml
import numpy as np
import bs4

def startPipeline():
    generator = pipeline('text-generation', model='gpt2')
    return generator

# Given a number letters and some sequence, returns the sequence with generated attached words
def generateText(generator,intro_sequence:str, num_words = 5)->str:
    # Imported random text generation
    text = generator(intro_sequence, max_length=len(intro_sequence) + num_words, num_return_sequences=1)[0].get("generated_text")
    return text

def getText(url = "https://www.keepinspiring.me/famous-quotes/" ):
    # Requesting data from url, finding specialized tags for this particular website
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    text  = soup.find_all("div", class_ = 'author-quotes')
    return text
text = getText()

#Tag processing functions to clean up nasty html formatting, replaces div tags
def processing_div(tag):
    return tag.replace('<div class="author-quotes">', "").replace("</div>", "")

#span processing, replaces span tag
def processing_span(tag):
    return tag.replace("<span class=\"quote-author-name\">", "").replace("</span>", "")

# Checks for tags that have yet to be removed, not given standard format. Reasoning - we don't know when ads will pop up
def cleaner(table):
    arr = np.array([])
    for i in table.get("quote"):
        arr = np.append(arr,("<" in i))
    clean = table[(arr != 1)]
    return clean

table = pd.DataFrame().assign(quote = text)

#Formatting, processing, and splitting quotes and authors
def tableProcess(table):
    table = table.assign(quote = table.get("quote").apply(str))
    table = table.assign(quote = table.get("quote").apply(processing_div).apply(processing_span))
    table = cleaner(table)
    table = table.assign(author  = table.get("quote").apply(authors), quote = table.get("quote").apply(removeAuthors))
    return table
table = tableProcess(table)
table

# Obtainin author from quote
def authors(quote):
    return quote.split("”")[1]

#Removing author and adding lost smartquote
def removeAuthors(quote):
    return (quote.split("”")[0] + ("”"))


import random


def replace_words_at_random(generator, word_arr: [str], num_words: int):
    # Pick num_words indices out of word_arr
    # Store the chosen indices
    indices = np.array([])
    for i in range(num_words):
        # Pick the next random index
        index = random.randint(3, len(word_arr) - 1)

        # Store the index of the next chosen word
        indices = np.append(indices, index)

        # Adding together everything leading up to string so as to add some context into the model
        join = " ".join(word_arr[:index])

        # Generate the next word
        text = generateText(generator, join, 10)

        # After sentence completed, we replace original string with the first word that the word generator came up with
        word_arr[index] = text.split(" ")[index]
    indices = np.unique(indices)
    return word_arr, indices

song = """Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you""".split(" ")
words = replace_words_at_random(startPipeline(), song, 12)

