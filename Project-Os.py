from collections import Counter 
import numpy as np
import string
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import io
import math
from pathlib import Path
from dataclasses import dataclass, field
from functools import lru_cache
from pypdf import PdfReader

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def read_document(note_file):
    suffix = Path(note_file).suffix.lower()     # ".txt" or ".pdf"

    if suffix == ".txt":
        with open(note_file, 'r', encoding='utf-8') as file:
            return file.read()

    if suffix == ".pdf":
        reader = PdfReader(note_file)
        # TODO: get the text from every page and join it into one string,
        # the same way as the "all_text" line in the pypdf example from earlier
        # TODO: anything else: print a clear message and return None


def clean_text(text):                               # takes ONE review string (that is what .apply passes in)
    text = re.sub('<.*?>', ' ', text)               # remove HTML tags like <br /> found in IMDB reviews
    text = re.sub('[^a-zA-Z0-9]', ' ', text)           # replace anything that is not a letter with a space
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
    
if __name__ == "__main__":
    note_file = input("Enter the path of the notes: ")
    text = read_document(note_file)
    if text:
        print(text[:300])                  # first 300 characters
        print(clean_text(text)[:20])       # first 20 cleaned words
