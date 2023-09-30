# coding: cp1252

'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 01
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 01")

print("\n ############# ################ ####################\n")

# Importing Stuff
import nltk as nlp
from nltk.stem import PorterStemmer as ps
import re
from nltk.stem import WordNetLemmatizer as WNL

# Function For Removing Punctuation
def no_punks(words):
    de_punked = []

    for x in words:
        still_punk = str(x)
        still_punk = re.sub(r'[^\w]', '', still_punk)
        de_punked.append(still_punk)
        
    return de_punked

# Function For Lower Case + Word Tokenization
def tolkein(sen):
    words = nlp.word_tokenize(sen)
    
    words = [word.lower() for word in words if word.isalpha()]
    
    return words

# Function For Removing Stop Words
def Stop_it(words):
    
    stop_these = {'all', 'below', 'ourselves', 'y', 'when', 'didn', 'into', 'being', 'whom', 'until', 'by', 'he', "hadn't", 'theirs', 'was', 'me', 'will', 'yours', 'just', 'to', 'where', 'm', 'wouldn', 'while', 'myself', "you'd", 're', 'now', 'mightn', 'again', 'is', 'there', "couldn't", 'am', 'how', 'so', 'ma', 'through', 'for', 'between', "that'll", 'o', 'no', 'does', 'here', 'not', 'or', "isn't", 'who', 'them', 'these', 've', 'his', 'himself', 'why', 'same', 'yourselves', 'doesn', 'then', 'it', 'over', 'from', 'd', 'hadn', 'most', "you'll", 'against', 'up', 'll', "shan't", 'once', "you've", 'very', 'own', 'haven', 'their', 'wasn', "doesn't", 'hers', 'aren', 'about', 'some', 'i', 'ain', "you're", "shouldn't", 'yourself', 'other', "hasn't", 'few', 'but', 'than', "didn't", 'under', 'shouldn', 'weren', 'can', 'do', 'as', 'won', 'with', 'what', 'itself', "won't", 'of', 'her', 't', 'this', 'has', "aren't", 'herself', 'mustn', 'both', "mightn't", 'did', 'further', 'been', 'needn', 'couldn', 'isn', "weren't", 'those', 'the', 'because', 'and', 'a', 'any', "wouldn't", 'shan', 'had', "wasn't", 'above', 'themselves', 'more', "it's", 'that', 'in', 'ours', 'should', 'off', 'have', 'at', 'we', "needn't", "don't", 'if', 'having', 's', 'its', "should've", 'she', 'such', 'down', 'on', 'were', "she's", 'doing', "haven't", 'him', 'after', 'my', 'out', 'nor', 'don', 'which', 'our', 'be', "mustn't", 'during', 'hasn', 'only', 'they', 'too', 'are', 'you', 'before', 'an', 'your', 'each'}
    
    words_have_been_stopped = [i for i in words if i not in stop_these]
    
    return words_have_been_stopped

# Function For Stemming
def Stem_it(words):
    
    stemmer = ps()
    stemmed = []
    
    for x in words:
        unstemmed = stemmer.stem(x)
        stemmed.append(unstemmed)
        
    return stemmed

# Function For Lemmatization
def Lemmat_it(words):
    
    llama = WNL()
    llama_d = []
    for w in words:
        llama_d.append(str(llama.lemmatize(w)))
        
    return llama_d

# Function For POS #
def Make_it_a_POS(words):
    
    Perfect_POS = []
    for z in words:
        tags = nlp.pos_tag(words)
        Perfect_POS.append(tags)
        
    return Perfect_POS

# Function For Counting Frequency #
def freakie(sen):
    freq = {}
    
    for z in sen:
        if str(z) not in freq.keys():
            freq[str(z)] = 1
        else:
            freq[str(z)] += 1
            
    return freq

data = str(["No one would have believed in the last years of the nineteenth century that this world was being watched keenly and closely by intelligences greater than man’s and yet as mortal as his own; that as men busied themselves about their various concerns they were scrutinised and studied, perhaps almost as narrowly as a man with a microscope might scrutinise the transient creatures that swarm and multiply in a drop of water. With infinite complacency men went to and fro over this globe about their little affairs, serene in their assurance of their empire over matter. It is possible that the infusoria under the microscope do the same. No one gave a thought to the older worlds of space as sources of human danger, or thought of them only to dismiss the idea of life upon them as impossible or improbable. It is curious to recall some of the mental habits of those departed days. At most terrestrial men fancied there might be other men upon Mars, perhaps inferior to themselves and ready to welcome a missionary enterprise. Yet across the gulf of space, minds that are to our minds as ours are to those of the beasts that perish, intellects vast and cool and unsympathetic, regarded this earth with envious eyes, and slowly and surely drew their plans against us. And early in the twentieth century came the great disillusionment."])

print(f"Original Text:\n\n{data}", end="\n\n")

lowered_token_data = tolkein(data)
print(f"Lower Cased and Tokenized:\n\n{lowered_token_data}", end="\n\n")

stopped_data = Stop_it(lowered_token_data)
print(f"Removing Stop Words:\n\n{stopped_data}", end="\n\n")

de_punked_data = no_punks(stopped_data)
print(f"Removing Punctuation:\n\n{de_punked_data}", end="\n\n")

stemmed_data = Stem_it(de_punked_data) # Break Off Point
print(f"Stemming the text:\n\n{stemmed_data}", end="\n\n")

llama_data = Lemmat_it(stemmed_data) # Break Off Point
print(f"Lemmatization Filtered Text :\n\n{llama_data}", end="\n\n")

POS_data = Make_it_a_POS(llama_data)
print(f"POS Text :\n{POS_data}", end="\n\n")

Freak_data = freakie(de_punked_data)
print(f"Frequency Chart of all the Words :\n\n{Freak_data}", end="\n\n")

# Cautiously Crafted By Redzwinger #

