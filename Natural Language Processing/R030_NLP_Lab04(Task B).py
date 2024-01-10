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

print("\n Task B")

print("\n ############# ################ ####################\n")

import numpy as np
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pandas as pd
from nltk import word_tokenize, sent_tokenize
import re
import string
import seaborn as sns

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

do_stuf = pd.read_csv("dataset.csv")
#pd.set_option('display.max_columns', None)

col = do_stuf.columns
print(col)
# columns = ['app_id', 'app_name', 'review_text', 'review_score', 'review_votes']

do_stuf.drop(columns=['app_id', 'review_votes'], inplace=True)
do_stuf.dropna(inplace=True)

print("\n\n Dataset contains reviews for various games from Steam:\n ", do_stuf.head(10), end="\n\n")

print(' Number of games:', len(do_stuf["app_name"].unique()), "\n From a total", len(do_stuf), "entries.", end="\n\n")

#do_stuf["review_text"].tolist()
plt.pie(do_stuf['review_score'].value_counts(),labels=['positive','negative'],autopct='%0.2f')
plt.show()

do_stuf = do_stuf.truncate(250, 10000)
print(" Truncating the database to", len(do_stuf), "enties:\n ", do_stuf,  end="\n\n")

do_stuf['char_num'] = do_stuf['review_text'].apply(len)
do_stuf.head(10)

do_stuf['word_num'] = do_stuf['review_text'].apply(lambda x: len(word_tokenize(x)))
do_stuf.head(10)

do_stuf['sent_num'] = do_stuf['review_text'].apply(lambda x: len(sent_tokenize(x)))
do_stuf.head(10)

do_stuf[['char_num','word_num','sent_num']].describe()

do_stuf[do_stuf['review_score'] == -1][['char_num','word_num','sent_num']].describe()
do_stuf[do_stuf['review_score'] == 1][['char_num','word_num','sent_num']].describe()

sns.histplot(do_stuf[do_stuf['review_score'] == 1]['char_num'])
sns.histplot(do_stuf[do_stuf['review_score'] == -1]['char_num'],color='red')
plt.show()

sns.histplot(do_stuf[do_stuf['review_score'] == 1]['word_num'])
sns.histplot(do_stuf[do_stuf['review_score'] == -1]['word_num'],color='red')
plt.show()

sns.histplot(do_stuf[do_stuf['review_score'] == 1]['sent_num'])
sns.histplot(do_stuf[do_stuf['review_score'] == -1]['sent_num'],color='red')
plt.show()

sns.pairplot(do_stuf,hue='review_score')
plt.show()

sns.heatmap(do_stuf.corr(),annot=True)
plt.show()

# Catatonically Crafted By Redzwinger #

