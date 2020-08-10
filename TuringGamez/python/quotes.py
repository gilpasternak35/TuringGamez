from typing import List
import pandas as pd
import numpy as np
from transformers.pipelines import Pipeline


# Runs the madlibs famous quotes version (returns messed up text)
def guessText_quotes_gameplay(nlp: Pipeline, level: int) -> str:
    # Scraping quotes website to obtain our text
    text = get_text()
    table = pd.DataFrame().assign(quote=text)
    table = table_process(table)

    # Selecting a random quote
    quotenum = np.random.randint(table.shape[0])
    row = table.iloc[quotenum]
    quote = row.get("quote").split(" ")
    author = row.get("author")
    # Randomly replacing words
    new_quote, indices = replace_words_at_random(nlp, quote, level)
    return new_quote + " " + author


# Runs the madlibs famous quotes version (returns messed up text)
def madlibs_quotes_gameplay(nlp: Pipeline, level: int) -> str:
    # Scraping quotes website to obtain our text
    text = get_text()
    table = pd.DataFrame().assign(quote=text)
    table = table_process(table)

    # Selecting a random quote
    quotenum = np.random.randint(table.shape[0])
    row = table.iloc[quotenum]
    quote = row.get("quote").split(" ")
    author = row.get("author")
    # Randomly replacing words
    new_quote, indices = replace_words_at_random(nlp, quote, level)
    return new_quote + " " + author


# Obtaining author from quote
def authors(quote: str) -> List[str]:
    return quote.split("”")[1]


# Removing author and adding lost smartquote
def remove_authors(quote: str) -> str:
    return quote.split("”")[0] + ("”")


# Tag processing functions to clean up nasty html formatting, replaces div tags
def processing_div(tag: str) -> str:
    return tag.replace('<div class="author-quotes">', "").replace("</div>", "")


# span processing, replaces span tag
def processing_span(tag: str) -> str:
    return tag.replace("<span class=\"quote-author-name\">", "").replace("</span>", "")


# Checks for tags that have yet to be removed, not given standard format. Reasoning - we don't know when ads will pop up
def cleaner(table: pd.DataFrame) -> pd.DataFrame:
    arr = np.array([])
    for i in table.get("quote"):
        arr = np.append(arr,("<" in i))
    clean = table[(arr != 1)]
    return clean


# Formatting, processing, and splitting quotes and authors
def table_process(table: pd.DataFrame) -> pd.DataFrame:
    table = table.assign(quote = table.get("quote").apply(str))
    table = table.assign(quote = table.get("quote").apply(processing_div).apply(processing_span))
    table = cleaner(table)
    table = table.assign(author  = table.get("quote").apply(authors), quote = table.get("quote").apply(remove_authors))
    return table