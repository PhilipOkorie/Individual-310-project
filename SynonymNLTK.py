from urllib.request import ProxyHandler
from nltk.corpus import wordnet as wn
from Chatbot import *


synonyms = []

def detectsyn(words):
    for word in words:
        for syn in wn.synsets(word):
            for w in syn.lemmas():
                synonyms.append(w.name())
    
    
    return synonyms


