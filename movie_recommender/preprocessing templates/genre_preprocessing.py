#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:34:28 2018

@author: vishal
"""

import pandas as pd
import ast

#only the useful columns are selected after writing the useful columns to
# a csv file
df=pd.read_csv("useful_without_chinese.csv")
df=df.drop(['Unnamed: 0'],axis=1)

#editing genre column and extracting the useful information only
df_genres=df['genres']

#converting series object to dataframe pandas
df_genres=df_genres.to_frame()

#iterating over dataframe
for index,rows in df_genres.iterrows():
#
    content=""
#iterating over every row using index    
    item=df_genres.iloc[index]['genres']
    #print(item)
    item=ast.literal_eval(item)
    for i in range(len(item)):
        content+=""+str(item[i]['name'])+","
    content=content[:-1]
    content=content.replace(" ","")
    content=content.replace(","," ")
    df_genres.iloc[index]['genres']=content
df_genres.to_csv('genres.csv')