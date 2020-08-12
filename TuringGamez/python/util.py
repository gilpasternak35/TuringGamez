from typing import List, Tuple
import requests 
import numpy as np
import bs4
from transformers.pipelines import Pipeline, pipeline

    # Starting up pipeline
    # Should do automatically upon starting program
    def start_pipeline() -> Pipeline:
        """ Function for one time start of Transformers pipeline, will be run by default at the beginning of the program

        Returns:
            Pipeline: [description]
        """
        generator = pipeline('fill-mask', model='bert-base-uncased')
        return generator

    # Given a number letters and some sequence, returns the sequence with generated attached words
    def generate_text(generator: Pipeline, intro_sequence: str, num_words = 5) -> str:
        """Generates a text sequence

        Args:
            generator (Pipeline): An instance of the Transformers pipeline (HuggingFace implementation) used to generate words
            intro_sequence (str): The initial text
            num_words (int, optional): Number of words to be replaced. Defaults to 5.

        Returns:
            str: [description]
        """
        # Imported random text generation
        text = generator(intro_sequence, max_length=len(intro_sequence) + num_words, num_return_sequences=1)[0]
        return text.get('generated_text')


    def replace_words_at_random(generator: Pipeline, word_arr: List[str], difficulty=1) -> Tuple[str, List[int]]:
        """[summary]

        Args:
            generator (Pipeline): [description]
            word_arr (List[str]): [description]
            difficulty (int, optional): [description]. Defaults to 1.

        Returns:
            Tuple[List[str], List[int]]: [description]
        """
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
    def random_generation(num_words: int, lowNum: int, highNum: int) -> int:
        """[summary]

        Args:
            num_words (int): [description]
            lowNum (int): [description]
            highNum (int): [description]

        Returns:
            int: [description]
        """
        random_digits = np.unique(np.random.randint(low=lowNum, high=highNum, size=num_words))
        while (len(random_digits) < num_words):
            random_digits = np.append(random_digits,
                                      np.random.randint(low=lowNum, high=highNum, size=num_words - len(random_digits)))
            random_digits = np.unique(random_digits)
        return random_digits