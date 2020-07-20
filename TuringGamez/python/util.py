from transformers import pipeline, set_seed
import requests
import numpy as np
import bs4


# Starting up pipeline
def start_pipeline():
    generator = pipeline('fill-mask', model='bert-base-uncased')
    return generator

# Given a number letters and some sequence, returns the sequence with generated attached words
def generate_text(generator,intro_sequence:str, num_words = 5)->str:
    # Imported random text generation
    text = generator(intro_sequence, max_length=len(intro_sequence) + num_words, num_return_sequences=1)[0].get("generated_text")
    return text

def get_text(url = "https://www.keepinspiring.me/famous-quotes/" ):
    # Requesting data from url, finding specialized tags for this particular website
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    text  = soup.find_all("div", class_ = 'author-quotes')
    return text


def replace_words_at_random(generator, word_arr: [str], difficulty=1) -> ([str], [int]):
    num_words = int(np.ceil((len(word_arr) * (1 / (2 * difficulty)))))
    #  Generate num_words random indices
    indices = random_generation(num_words, 0, len(word_arr))
    print(indices)

    # Place word masks at each of the randomly chosen indices
    # Fill in each mask with the language model
    for i in indices:
        # Ensuring array is not over-accessed
        if (i < len(word_arr)):
            word_arr[i] = '[MASK]'

        # Adding together everything leading up to string so as to add some context into the model
        join = " ".join(word_arr)

        # Generate the next word
        text = (generator(join)[5 - difficulty].get('sequence').replace("[CLS]", '').replace('[SEP]', '')).strip()
        word_arr = text.split(" ")

    return text, indices


# Generates a desired number of unique random digits in a certain range
def random_generation(num_words, lowNum, highNum):
    random_digits = np.unique(np.random.randint(low=lowNum, high=highNum, size=num_words))
    while (len(random_digits) < num_words):
        random_digits = np.append(random_digits,
                                  np.random.randint(low=lowNum, high=highNum, size=num_words - len(random_digits)))
        random_digits = np.unique(random_digits)
    return random_digits