#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:20:04 2018

@author: vishal
"""

import pandas as pd
from difflib import get_close_matches
import numpy as np
df=pd.read_csv("cosine_matrix.csv")
df=df.drop("Unnamed: 0",axis=1)
df_pwu=pd.read_csv("final_processed_with_urls.csv")
df_titles=df_pwu['titles']
counter=1
while counter==1:
    name_of_movie=input("write the name of the movie")
    k=get_close_matches(name_of_movie,df_titles)
    df_cosine_matrix=pd.read_csv("cosine_matrix.csv")
    df_cosine_matrix=df_cosine_matrix.drop("Unnamed: 0",axis=1)
    index_list=[]
    titles_list=[]
    urls_list=[]
    if not k:
        print("not in database currently")
    else:
        print(k[0])
        num=df_titles[df_titles==k[0]].index[0]
        num=np.asscalar(num)
        index_of_movie=str(num)
        df_movie_to_show=df_cosine_matrix[index_of_movie]
        df_top_5=df_movie_to_show.nlargest(6)
        df_top_5=df_top_5.to_frame()
        for index, row in df_top_5.iterrows():
            index_list.append(index)

    for i in range(1,6):
        titles_list.append(df_pwu.iloc[index_list[i]]['titles'])
        urls_list.append(df_pwu.iloc[index_list[i]]['urls'])
    #print(urls_list)
    print (titles_list)
