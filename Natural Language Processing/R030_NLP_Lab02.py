'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 02
Date: 10/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 02 \n Date: 10/08/2023")

print("\n ############# ################ ####################\n")

# importing stuff
from symtable import SymbolTable
import numpy  as np
from nltk import word_tokenize
from sklearn import preprocessing as pre
import pandas as pd

def tolkein(sen):
    words = word_tokenize(sen)
    words = [word.lower() for word in words if word.isalpha()]
    return words

sentences = "I am Optimus Prime, and I send this message to any surviving Autobots taking refuge among the stars. We are here. We are waiting."

sentence =["I am Optimus Prime, and I send this message to any surviving Autobots taking refuge among the stars.", "We are here." "We are waiting."]

t = tolkein(sentences)
print(" Tokenized Data: \n", t)

label_encoder = pre.LabelEncoder()

label = label_encoder.fit_transform(t)
dicty = dict()

for i in range(len(t)):
    dicty[t[i]] = label[i]
print("\n Label Encoded: \n",dicty)

fixed_label = label.reshape(len(label),1)

encoderMan = pre.OneHotEncoder(sparse=False)
Hottie = encoderMan.fit_transform(fixed_label)
print("\n One Hot Encoded Data:\n",Hottie)

statement_of_a_lifetime = "I am Optimus Prime, and I send this message so that our pasts will always be remembered."

print("\n Another Sentence:\n", statement_of_a_lifetime)

def bowBOW(testy, words):
    sentence_words = tolkein(testy)
    
    bag = np.zeros(len(words))
    
    for sw in sentence_words:
        for i,word in enumerate(words):
            if word == sw: 
                bag[i] += 1
                
    for x in range(len(words)):
        print(f"Word: \t{words[x]} \t\tFrequency: {bag[x]}")
   
BOW = bowBOW(statement_of_a_lifetime, t)

from sklearn.feature_extraction.text import TfidfVectorizer
IDEAF_model  = TfidfVectorizer()
IDEAF_vector = IDEAF_model.fit_transform(sentence)

print("\n ", type(IDEAF_vector), IDEAF_vector.shape)

IDEAf_Array = IDEAF_vector.toarray()
print(IDEAf_Array)
thingu = IDEAF_model.get_feature_names_out()
IDEAF_Dataframe =pd.DataFrame(IDEAf_Array, columns=thingu)

print("\n IDFT:\n", IDEAF_Dataframe)

