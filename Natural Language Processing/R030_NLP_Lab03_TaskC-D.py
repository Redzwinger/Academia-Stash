'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 03
Date: 10/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 03 \n Date: 10/08/2023")

print("\n Task C+D")

print("\n ############# ################ ####################\n")

import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize

# Using Brown Corpus for various NLP Processes NLTK

# Function for doing stuff
def BrownIsGood():
    # Accessing Brown corpus from nltk
    alltexts = brown.fileids()
    categor = brown.categories()
    print(" Accesssing and Listing all the texts from the Brown Corpus through NLTK: \n", alltexts, end="\n\n")
    
    for c in categor:
        words = brown.words(categories=c)
        print(" Category: ",c, "\n Total Number of Words: \n", len(words), end="\n\n")
        
        sentences = brown.sents(categories=c)
        print(" Total Number of Sentences: \n", len(sentences), end="\n\n")
        
        freqdist = nltk.FreqDist(w.lower() for w in words)
        print(" Frequency Distribution: \n", freqdist, end="\n\n")

BrownIsGood()

# Curiously Crafted By Redzwinger #

