from transformers import pipeline, set_seed
import pandas as pd
import requests, sys, webbrowser,xml
import numpy as np
import bs4
import re
import random
from urllib.error import HTTPError
import argparse

def main():
    # Will return individual elements
    parser = argparse.ArgumentParser(description = "TuringGamez")
    # Parsing string and passing it to decider function, which will


