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

print("\n Task G+H")

print("\n ############# ################ ####################\n")

import nltk as nlp
from nltk.tokenize import word_tokenize
from urllib import request
from nltk.collocations import *

def tolkein(sen):
    words = nlp.word_tokenize(sen)
    
    words = [word.lower() for word in words if word.isalpha()]
    
    return words

# Function for doing stuff
def HTMLIsBad():
    # Accessing texts from the web
    url = "https://www.gutenberg.org/cache/epub/2097/pg2097-images.html"
    response = request.urlopen(url)
    raw = response.read().decode('utf8')
    
    print(" Accesssing Text from the html: \n", raw, end="\n\n")
    
    words = tolkein(raw)
    print("\n Tokenized Words: \n", words, end="\n\n")
    
    text = nlp.Text(nlp.word_tokenize(raw))

    searchit = str('Sherlock')
    print("\n Concording '",searchit,"' : \n", end="\n")
    findit = text.concordance(searchit)

HTMLIsBad()

# Curiously Crafted By Redzwinger #