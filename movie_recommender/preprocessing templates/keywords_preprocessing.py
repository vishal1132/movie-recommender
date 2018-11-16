#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:45:39 2018

@author: vishal
"""

import pandas as pd
import ast

#only the useful columns are selected after writing the useful columns to
# a csv file
df=pd.read_csv("useful_without_chinese.csv")
df=df.drop(['Unnamed: 0'],axis=1)

#editing genre column and extracting the useful information only
df_keywords=df['keywords']

#converting series object to dataframe pandas
df_keywords=df_keywords.to_frame()

for index,rows in df_keywords.iterrows():
    content=""
    item=df_keywords.iloc[index]['keywords']
    item=ast.literal_eval(item)
    for i in range(len(item)):
        content+=""+str(item[i]['name'])+","
    content=content[:-1]
    content=content.replace(" ","")
    content=content.replace(","," ")
    df_keywords.iloc[index]['keywords']=content    
df_keywords.to_csv('keywords.csv')  