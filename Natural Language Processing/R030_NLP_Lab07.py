'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 06
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 06")

print("\n Task B")

print("\n ############# ################ ####################\n")

import nltk
import spacy
from nltk.tokenize import word_tokenize
import re
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def no_punks(words):    
    de_punked = []

    for x in words:
        still_punk = str(x)
        still_punk = re.sub(r'[^\w]', '', still_punk)
        de_punked.append(still_punk)
        
    return de_punked

def Stop_it(words):
    
    stop_these = {'all', 'below', 'ourselves', 'y', 'when', 'didn', 'into', 'being', 'whom', 'until', 'by', 'he', "hadn't", 'theirs', 'was', 'me', 'will', 'yours', 'just', 'to', 'where', 'm', 'wouldn', 'while', 'myself', "you'd", 're', 'now', 'mightn', 'again', 'is', 'there', "couldn't", 'am', 'how', 'so', 'ma', 'through', 'for', 'between', "that'll", 'o', 'no', 'does', 'here', 'not', 'or', "isn't", 'who', 'them', 'these', 've', 'his', 'himself', 'why', 'same', 'yourselves', 'doesn', 'then', 'it', 'over', 'from', 'd', 'hadn', 'most', "you'll", 'against', 'up', 'll', "shan't", 'once', "you've", 'very', 'own', 'haven', 'their', 'wasn', "doesn't", 'hers', 'aren', 'about', 'some', 'i', 'ain', "you're", "shouldn't", 'yourself', 'other', "hasn't", 'few', 'but', 'than', "didn't", 'under', 'shouldn', 'weren', 'can', 'do', 'as', 'won', 'with', 'what', 'itself', "won't", 'of', 'her', 't', 'this', 'has', "aren't", 'herself', 'mustn', 'both', "mightn't", 'did', 'further', 'been', 'needn', 'couldn', 'isn', "weren't", 'those', 'the', 'because', 'and', 'a', 'any', "wouldn't", 'shan', 'had', "wasn't", 'above', 'themselves', 'more', "it's", 'that', 'in', 'ours', 'should', 'off', 'have', 'at', 'we', "needn't", "don't", 'if', 'having', 's', 'its', "should've", 'she', 'such', 'down', 'on', 'were', "she's", 'doing', "haven't", 'him', 'after', 'my', 'out', 'nor', 'don', 'which', 'our', 'be', "mustn't", 'during', 'hasn', 'only', 'they', 'too', 'are', 'you', 'before', 'an', 'your', 'each'}
    
    words_have_been_stopped = [i for i in words if i not in stop_these]
    
    return words_have_been_stopped

def tolkein(sen):
    #words = sent_tokenize(sen)
    words = word_tokenize(sen)
    words = [word.lower() for word in words if word.isalpha()]
    return words

def pos(words):
    pos_tags = nltk.pos_tag(words)
    return pos_tags

sample_text = pd.read_csv("")

tokens = tolkein(sample_text)
tokens_no_punks = no_punks(tokens)
tokens_no_stopwords = Stop_it(tokens_no_punks)

# POS tagging using NLTK
pos_tags = nltk.pos_tag(tokens_no_stopwords)

# Named Entity Recognition using NLTK
named_entities = nltk.ne_chunk(pos_tags)

# POS tagging and Named Entity Recognition using SpaCy
doc = nlp(str(tokens_no_stopwords))

# Extracting named entities and their labels from SpaCy
named_entities_spacy = [(entity.text, entity.label_) for entity in doc.ents]

print(" NLTK POS Tags:\n", pos_tags, end="\n\n")
print(" NLTK Named Entities:\n", named_entities, end="\n\n")
print(" SpaCy Named Entities:\n", named_entities_spacy, end="\n\n")

# Chaotically Crafted By Redzwinger #

