#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:44:33 2018

@author: vishal
"""

import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df=pd.read_csv('final_processed_with_urls.csv')
df=df.drop("Unnamed: 0",axis=1)
df=df.rename(columns={"0":"bag_of_words"})
count=CountVectorizer()
count_matrix=count.fit_transform(df['bag_of_words'])
cosine_sim=cosine_similarity(count_matrix,count_matrix)
print(type(cosine_sim))
dff=pd.DataFrame(cosine_sim)

dff.to_csv("cosine_matrix.csv")

'''
df_title=pd.read_csv("lowercase_titles.csv")
df_title=df_title.drop('Unnamed: 0',axis=1)
df_title=df_title.iloc[:,0]
title=input("name the movie you watched recently")
title=title.lower()
index=df_title[df_title==title]
print(index)
'''