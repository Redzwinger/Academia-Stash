'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 09
Date: 19/10/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 09 \n Date: 19/10/2023")

print("\n ############# ################ ####################\n")

import pandas as pd

maiden_less = pd.read_csv("elden_ring_steam_reviews.csv")
print(" Selected Dataset contains reviews from Steam for the game Elden Ring:\n\n ", maiden_less, end="\n\n")

print(maiden_less.columns)

dropped_yet_still_maiden_less = maiden_less.drop(['created', 'voted_up', 'votes_up', 'comment_count', 'steam_purchase', 'recieved_for_free', 'written_during_early_access', 'author_num_games_owned', 'author_last_played'], axis=1)

print(" Removing unnescessay information:\n\n ", dropped_yet_still_maiden_less, end="\n\n")