from collections import Counter 
import numpy as np
import string
import re
import nltk
from nltk.stem import WordNetLemmatizer
import io
import math
from pathlib import Path
from dataclasses import dataclass, field
from functools import lru_cache
from pypdf import PdfReader

lemmatizer = WordNetLemmatizer
note_file = input("Enter the path of the notes: ")

def analyse_words(note_file):
    with open(note_file, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower()
        clean_


def clean_text(text):                               # takes ONE review string (that is what .apply passes in)
    text = re.sub('<.*?>', ' ', text)               # remove HTML tags like <br /> found in IMDB reviews
    text = re.sub('[^a-zA-Z]', ' ', text)           # replace anything that is not a letter with a space
    text = text.lower()                             # lowercase so "Movie" and "movie" are the same word
    words = nltk.word_tokenize(text)                # split the review into a list of words (tokens)
    words = [word for word in words if word not in stop_words]   # keep every word that is not a stopword
    return words                                    # return the list of cleaned words

def lemma_words(words):                             # takes the list of words from clean_text
    words = [lemmatizer.lemmatize(word) for word in words]       # reduce each word to its dictionary form
    return ' '.join(words)                          # join the words back into one string for the vectorizers

def avg_word2vec(text):
    vecs = [w2v.word for word in text.split() if word in w2v.wv]
    if vecs: 
        return np.mean(vecs, axis = 0)
    else:
        return np.zeros(w2v.w2.vector_size)
