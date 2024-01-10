# Program Code for NLP Practicum #
# Made by Omkar Iyer [R022] & Achintya Kamath [R030] #
# MBA Tech Artificial Intelligence #

print("""
\t\tPracticum for NLP

Designed by Omkar Iyer [R022] & Achintya Kamath [R030]

Task : To Make a Simple Spell Checker using NLTK Library

""")



# First Importing the Libraries
import nltk
from nltk.metrics.distance import edit_distance as distance

# It is assumed that you have downloaded "words"
# If not, then run this >>> nltk.download('words')

from nltk.corpus import words

# Function for detecting the error
def giveError(listOfWords):
    goodWords = words.words()
    for w in listOfWords:
        best_match = min(goodWords, key=lambda word: distance(w, word))
        print(f"Suggested correction for '{w}': {best_match}")

# Testing the Function
randomIn = input("\nType Something -> ").split()
giveError(randomIn)

# Programmed by Orbia343 & Redzwinger #
