# goal: create a co-occurence matrix that shows the frequency of paired elements

from collections import Counter
import itertools
from itertools import chain, combinations

import pandas as pd
import numpy as np

import ssl
from chord import Chord

df = pd.read_csv("cocktails_final.csv")

pairs = df.groupby(['row_id'])['Ingredient'].apply(list).tolist()  # make a list of a lists of ingredients that are in each cocktail

pair_dict = Counter(chain.from_iterable(combinations(pair, 2) for pair in pairs)) # convert list of lists into list of dictionary that count frequency for each unique pair

common = df['Ingredient'].value_counts()[:29].index.tolist() # list of top ingredients in 'ingredient' column

common_set = set(common)
new_pairs = {}
for key in pair_dict.keys():                                # iterate across all keys
    key1, key2 = key                                        # for each key (a tuple), split key into 2 variables by comma
    if key1 in common_set and key2 in common_set:           # if both elements in tuple (key) are found in list
        new_pairs[key] = pair_dict[key]                     # put this key (and its paired value) into a new dictionary (new_pairs)



# check if certain element is in new dictionary
#if (any('Sweet and sour' in i for i in new_pairs)):
#    print('True')
#else:
#    print('False')

key1 = np.array(list(new_pairs.keys()))
vals = np.array(list(new_pairs.values()))

uniq_key1, key1_index = np.unique(key1, return_inverse=True)
uniq_key0 = list(uniq_key1)


key1_index = key1_index.reshape(-1,2)
n = len(uniq_key0)
matrix = np.zeros((n, n), dtype=vals.dtype)
matrix[key1_index[:,0], key1_index[: ,1]] = vals
matrix += matrix.T
matrix=matrix.tolist()

color_list = ["#ff7518", "#C68E17", "#43182f", "#D2691E", "#B5651D", "#4f86f7", "#cf350e", "#622A0F", "#950714", "#3B270C", "#E1DABB", "#F9E5BC", "#D7C5A9", "#db1f1f", "#43270F", "#e8ce25", "#F9E5BC", "#bb9351", "#5ce825", "#ffe5b4", "#ffa500", "#e6ae25", "#ae9f80", "#D2691E", "#F9E5BC", "#ebb028", "#ff7518", "#ffe5b4", "#E1DABB"]


Chord(matrix, uniq_key0, colors=color_list, width=780, font_size_large=10, margin=150, wrap_labels=False).to_html("cocktail_chord.html")
