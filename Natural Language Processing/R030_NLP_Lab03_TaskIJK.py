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

print("\n Task I+J+K")

print("\n ############# ################ ####################\n")

import nltk as nlp
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud as wc, STOPWORDS
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from PIL import Image
from os import path
import random

def grey_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

def tolkein(sen):
    words = nlp.word_tokenize(sen)
    words = [word.lower() for word in words if word.isalpha()]
    return words

# Function for doing stuff
def LocalIsTheBest():
    # Accessing texts from the web
    txt = open("The Sign Of Four.txt", encoding="utf8")
    raw = txt.read()
    
    print(" Accesssing Text from local file: \n", raw, end="\n\n")
    
    words = tolkein(raw)
    print("\n Tokenized Words: \n", words, end="\n\n")
    
    mask = np.array(Image.open("shh.jpg"))
    
    stoppedwords = set(STOPWORDS)    
    WC = wc(max_words=1000, mask=mask, stopwords=stoppedwords, margin=10,random_state=1).generate(raw)
    
    rcParams["figure.figsize"] = (10,5)
    plt.imshow(WC, interpolation="bilinear")
    plt.axis("off")
    plt.show()

LocalIsTheBest()

# Curiously Crafted By Redzwinger #