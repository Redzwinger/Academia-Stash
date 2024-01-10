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

print("\n Task A+B")

print("\n ############# ################ ####################\n")

import nltk
from nltk.tokenize import word_tokenize

# Using Project Gutenberg (https://www.gutenberg.org/) for various NLP Processes

# Function for doing stuff
def GutenIsGood():
    # Accessing Gutenberg corpus from nltk
    alltexts = nltk.corpus.gutenberg.fileids()
    print(" Accesssing and Listing all the texts from the Gutenberg Corpus through NLTK: \n", alltexts, end="\n\n")
    
    for t in alltexts:
        raw = nltk.corpus.gutenberg.raw(t)
        print(" ",t, "\n Total Number of Words: \n", len(raw), end="\n\n")
        
        words = nltk.corpus.gutenberg.words(t)
        print(" Number of Unique Words: \n", len(words), end="\n\n")
        
        sentences = nltk.corpus.gutenberg.sents(t)
        print(" Total Number of Sentences: \n", len(sentences), end="\n\n")
        
        characters = word_tokenize(raw)
        total_characters = sum(len(characters) for characters in characters)
        average_cha = total_characters/len(words)
        print(" Average Characters Per Words: \n", average_cha, end="\n\n")
        
        total_tokens = len(characters)
        unique_types = len(set(characters))
        TTR = unique_types / total_tokens
        
        if TTR < 0.03:
            comment = "Low Lexical Richness - Limited Vocabulary Diversity."
        elif 0.03 <= TTR < 0.07:
            comment = "Moderate Lexical Richness - Some Vocabulary Diversity."
        else:
            comment = "High Lexical Richness - Extensive Vocabulary Diversity."
            
        print(" TTR Ratio: ", TTR, "\n",comment, end="\n\n")
      
GutenIsGood()

# Curiously Crafted By Redzwinger #


