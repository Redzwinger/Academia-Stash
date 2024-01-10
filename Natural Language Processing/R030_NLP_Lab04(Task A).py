'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 04
Date: 24/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 04 \n Date: 24/08/2023")

print("\n Task A")

print("\n ############# ################ ####################\n")

from nltk.corpus import PlaintextCorpusReader as pltxcr
import nltk
import numpy as np
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.util import ngrams
import pandas as pd
from nltk import word_tokenize, pos_tag, sent_tokenize
import re
import string
import math
from nltk.stem import WordNetLemmatizer

def tolkein(sen):
    words = word_tokenize(sen)
    words = [x for x in words if not re.fullmatch('[' + string.punctuation + ']+', x)]
    words = [word.lower() for word in words if word.isalpha()]
    return words

def stp_wrd(paragraph):
    stops = list(stopwords.words('english'))
    m_para = [i for i in paragraph if i not in stops]
    return m_para

def punky(paragraph):
    no_no = ["!","@","#","$","%","^","&","*",",",".","/",":",";","'","",","]
    good_stuff = [i for i in paragraph if i not in no_no]
    return good_stuff

def LocalIsTheBest():
    # Accessing texts from the text file
    txt = open("The Sign Of Four.txt", encoding="utf8")
    raw = txt.read()
    
    print(" Accesssing Text from local file: \n", raw[:1000],"...", end="\n\n")
    
    words = tolkein(raw)
    punk_words = punky(words)
    stopped_words = stp_wrd(punk_words)
    print("\n Tokenized Words: \n", stopped_words[:50], end="\n\n")
    print("\n Frequency Distribution:", end="\n\n")
    
    word = list(set(words))
    
    freq = [words.count(i) for i in word]
    print(" Total Words: ", len(freq), end="\n\n")
    df = pd.DataFrame(list(zip(word, freq)),columns =['Name', 'val'])
    
    print(df)
    
    thingy = " ".join(word)
    chap = thingy.split("Chapter")    
    
    chap_size = [len(i.split(" ")) for i in chap]
    
    average_chapter_len = int(sum(chap_size)/len(chap_size))
    
    print("\n Average Chapter Length:", average_chapter_len, end="\n\n")
    
    bi = list(ngrams(words,2))
    bi_list = list(set(bi))
    print(' Number of Bigrams:' ,len(bi_list), end="\n\n")
    
    tri = list(ngrams(words,3))
    tri_list = list(set(tri))
    print(' Number of Trigrams:' ,len(tri_list), end="\n\n")
    
    quad = list(ngrams(words,4))
    quad_list = list(set(quad))
    print(' Number of Quadgrams:' ,len(quad_list), end="\n\n")
    
LocalIsTheBest()

# Catatonically Crafted By Redzwinger #


