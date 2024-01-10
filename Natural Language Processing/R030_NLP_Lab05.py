'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 05
Date: 21/09/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 05 \n Date: 21/09/2023")

print("\n ############# ################ ####################\n")

# Word Embbeddings #

# Word2Vec and Glove #
# Take any 2 paragraphs use word2vec and find simialrity between the paragraphs #

# Doing Stuff #

from nltk.corpus.reader import PARA
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import numpy as np
import re
from gensim.models import Word2Vec
 
warnings.filterwarnings(action = 'ignore')

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
        
para_of_the_graphOne = str("We met next day as he had arranged, and inspected the rooms at No. 221B, Baker Street, of which he had spoken at our meeting. They consisted of a couple of comfortable bed-rooms and a single large airy sitting-room, cheerfully furnished, and illuminated by two broad windows. So desirable in every way were the apartments, and so moderate did the terms seem when divided between us, that the bargain was concluded upon the spot, and we at once entered into possession. That very evening I moved my things round from the hotel, and on the following morning Sherlock Holmes followed me with several boxes and portmanteaus. For a day or two we were busily employed in unpacking and laying out our property to the best advantage. That done, we gradually began to settle down and to accommodate ourselves to our new surroundings.")

graph_of_the_paraTwo = str("Holmes was certainly not a difficult man to live with. He was quiet in his ways, and his habits were regular. It was rare for him to be up after ten at night, and he had invariably breakfasted and gone out before I rose in the morning. Sometimes he spent his day at the chemical laboratory, sometimes in the dissecting-rooms, and occasionally in long walks, which appeared to take him into the lowest portions of the City. Nothing could exceed his energy when the working fit was upon him; but now and again a reaction would seize him, and for days on end he would lie upon the sofa in the sitting-room, hardly uttering a word or moving a muscle from morning to night. On these occasions I have noticed such a dreamy, vacant expression in his eyes, that I might have suspected him of being addicted to the use of some narcotic, had not the temperance and cleanliness of his whole life forbidden such a notion.")

tolkeinOne = tolkein(para_of_the_graphOne)
stoppedOne = Stop_it(tolkeinOne)
One = no_punks(stoppedOne)
print(" Word Pre-Processed Paragraph 1: ", One, end="\n\n")

tolkeinTwo = tolkein(graph_of_the_paraTwo)
stoppedTwo = Stop_it(tolkeinTwo)
Two = no_punks(stoppedTwo)
print(" Word Pre-processed Paragraph 2: ",Two, end="\n\n")

model = Word2Vec(sentences=(One,Two), min_count = 1, vector_size = 100, window = 5)

print("\n\n ----Word Similarity----\n\n")

for wordOne in One:
    for wordTwo in Two:
        simi = model.wv.similarity(wordOne, wordTwo)
        print(f" Similarity Coefficient Between '{wordOne}' and '{wordTwo}': \t\t", simi)
        
# Document Similarity

para_of_the_graphThree = [str("We met next day as he had arranged, and inspected the rooms at No. 221B, Baker Street, of which he had spoken at our meeting. They consisted of a couple of comfortable bed-rooms and a single large airy sitting-room, cheerfully furnished, and illuminated by two broad windows. So desirable in every way were the apartments, and so moderate did the terms seem when divided between us, that the bargain was concluded upon the spot, and we at once entered into possession. That very evening I moved my things round from the hotel, and on the following morning Sherlock Holmes followed me with several boxes and portmanteaus. For a day or two we were busily employed in unpacking and laying out our property to the best advantage. That done, we gradually began to settle down and to accommodate ourselves to our new surroundings.")]

graph_of_the_paraFour = [str("Holmes was certainly not a difficult man to live with. He was quiet in his ways, and his habits were regular. It was rare for him to be up after ten at night, and he had invariably breakfasted and gone out before I rose in the morning. Sometimes he spent his day at the chemical laboratory, sometimes in the dissecting-rooms, and occasionally in long walks, which appeared to take him into the lowest portions of the City. Nothing could exceed his energy when the working fit was upon him; but now and again a reaction would seize him, and for days on end he would lie upon the sofa in the sitting-room, hardly uttering a word or moving a muscle from morning to night. On these occasions I have noticed such a dreamy, vacant expression in his eyes, that I might have suspected him of being addicted to the use of some narcotic, had not the temperance and cleanliness of his whole life forbidden such a notion.")]

RL1 = [str("Rajesh loves playing football. he played football hours together today without taking rest")]

RL2 = [str("Football Athletes play their matches for hours together, without any breaks in between")]

model2 = Word2Vec(sentences=(para_of_the_graphThree,graph_of_the_paraFour),min_count = 1, vector_size = 4, window = 1)

print("\n\n ----Document Similarity----\n\n")

for StuffOne in para_of_the_graphThree:
    for StuffTwo in graph_of_the_paraFour:
        simi2 = model2.wv.similarity(StuffOne, StuffTwo)
        print(f" Similarity Coefficient Between Document 1:\n '{StuffOne}'\n\n and Document 2:\n '{StuffTwo}'\n\n is: ", simi2,end="\n\n")

# Chaotically Crafted By Redzwinger #

